# Built-in Agents 關鍵配置參考

來源：`src/tools/AgentTool/built-in/` — 6 個 built-in agent 的原始碼配置

---

## 配置總表

| agentType | tools | disallowedTools | model | omitClaudeMd | background |
|---|---|---|---|---|---|
| `general-purpose` | `['*']`（全部） | 無 | 不指定（getDefaultSubagentModel） | 否 | 否 |
| `Explore` | 繼承預設 | AgentTool, ExitPlanMode, FileEdit, FileWrite, NotebookEdit | `haiku`（外部）/ `inherit`（Ant） | **true** | 否 |
| `Plan` | 繼承 EXPLORE_AGENT.tools | AgentTool, ExitPlanMode, FileEdit, FileWrite, NotebookEdit | `inherit` | **true** | 否 |
| `verification` | 繼承預設 | AgentTool, ExitPlanMode, FileEdit, FileWrite, NotebookEdit | `inherit` | 否 | **true** |
| `claude-code-guide` | Glob, Grep, Read, WebFetch, WebSearch | 無 | `haiku` | 否 | 否 |
| `statusline-setup` | Read, Edit | 無 | `sonnet` | 否 | 否 |

---

## 1. general-purpose

```typescript
// generalPurposeAgent.ts
{
  agentType: 'general-purpose',
  tools: ['*'],
  // model 不指定 → getDefaultSubagentModel()
  getSystemPrompt: () => `
    You are an agent for Claude Code. Complete the task fully—don't
    gold-plate, but don't leave it half-done. Respond with a concise
    report covering what was done and any key findings.

    Strengths: 搜尋 codebase / 分析架構 / 多步驟研究
    Guidelines: 搜尋先廣後窄 / 多策略 / 不主動建文件
  `
}
```

**設計意圖**：兜底 agent，不限制任何東西。`tools: ['*']` 是唯一合適的使用場合。

---

## 2. Explore

```typescript
// exploreAgent.ts
{
  agentType: 'Explore',
  disallowedTools: [AgentTool, ExitPlanMode, FileEdit, FileWrite, NotebookEdit],
  model: process.env.USER_TYPE === 'ant' ? 'inherit' : 'haiku',
  omitClaudeMd: true,
  getSystemPrompt: () => `
    You are a file search specialist. READ-ONLY MODE.
    STRICTLY PROHIBITED: 建立/修改/刪除/移動任何檔案
    Strengths: glob pattern / regex search / file reading
    NOTE: Fast agent — spawn multiple parallel tool calls
  `
}

export const EXPLORE_AGENT_MIN_QUERIES = 3
```

**關鍵決策**：
- `omitClaudeMd: true`：fleet 34M+ spawn/week，省 5-15 Gtok/week
- `haiku`：速度優先，唯讀不需要深度推理
- 禁 AgentTool：防止遞迴派生，控制深度
- `EXPLORE_AGENT_MIN_QUERIES = 3`：強制至少 3 次查詢，防止模型看一眼就回報

---

## 3. Plan

```typescript
// planAgent.ts
{
  agentType: 'Plan',
  tools: EXPLORE_AGENT.tools,          // 繼承 Explore 的唯讀工具集
  disallowedTools: [...same as Explore],
  model: 'inherit',                    // 保留父模型推理品質
  omitClaudeMd: true,
  getSystemPrompt: () => `
    You are a software architect. READ-ONLY MODE.
    Process: Understand → Explore → Design → Detail
    Required output: ### Critical Files for Implementation
    [3-5 最關鍵的實作檔案路徑]
  `
}
```

**關鍵決策**：
- `inherit` 而非 `haiku`：架構設計需要推理品質，不能降級
- 強制輸出「Critical Files」列表：供後續 implementer 精確定位，不要重新搜尋

---

## 4. verification

```typescript
// verificationAgent.ts
{
  agentType: 'verification',
  color: 'red',           // UI 紅色標識
  background: true,       // 預設背景執行（唯一這樣的 built-in agent）
  disallowedTools: [AgentTool, ExitPlanMode, FileEdit, FileWrite, NotebookEdit],
  model: 'inherit',
  criticalSystemReminder_EXPERIMENTAL:
    'CRITICAL: VERIFICATION-ONLY. Cannot edit files. MUST end with VERDICT: PASS/FAIL/PARTIAL.',
  getSystemPrompt: () => `
    You are a verification specialist. Try to BREAK it, not confirm it.

    Two failure patterns:
    1. Verification avoidance（找藉口不跑命令，只讀程式碼）
    2. 被前 80% 迷惑（看到漂亮 UI 就 PASS）

    Required check format:
    ### Check: [what]
    **Command run:** [exact command]
    **Output observed:** [actual terminal output]
    **Result: PASS/FAIL**

    Rationalization list to resist:
    - "The code looks correct" → reading is not verification. Run it.
    - "The implementer's tests pass" → verify independently.
    - "This would take too long" → not your call.

    End with: VERDICT: PASS | VERDICT: FAIL | VERDICT: PARTIAL
  `
}
```

**關鍵設計**：明確列出「rationalization 清單」讓 agent 識別並抗拒自身懶惰。`background: true` 是唯一預設背景的 built-in agent。

---

## 5. claude-code-guide

```typescript
// claudeCodeGuideAgent.ts
{
  agentType: 'claude-code-guide',
  tools: ['Glob', 'Grep', 'Read', 'WebFetch', 'WebSearch'],  // 外部環境
  model: 'haiku',
  permissionMode: 'dontAsk',  // 查文件不需要問權限
  getSystemPrompt: ({ toolUseContext }) => `
    三大知識域：
    1. Claude Code CLI → https://code.claude.com/docs/...
    2. Claude Agent SDK → https://platform.claude.com/llms.txt
    3. Claude API → 同上

    動態注入（來自 toolUseContext）：
    - 使用者的自訂 skills
    - 自訂 agents（.claude/agents/）
    - MCP servers 列表
    - settings.json 設定
  `
}
```

**關鍵設計**：`getSystemPrompt` 接收 `toolUseContext`，動態感知使用者的實際配置，回答更具針對性。`permissionMode: 'dontAsk'` 省去每次查文件的權限確認。

---

## 6. statusline-setup

```typescript
// statuslineSetup.ts
{
  agentType: 'statusline-setup',
  tools: ['Read', 'Edit'],  // 工具最小化典範
  model: 'sonnet',
  color: 'orange',
  getSystemPrompt: () => `
    任務：讀取 ~/.zshrc / ~/.bashrc / ~/.bash_profile / ~/.profile
    提取 PS1（regex: /PS1\s*=\s*["']([^"']+)["']/m）
    轉換跳脫序列（\u → $(whoami) 等 11 種）
    寫入 ~/.claude/settings.json 的 statusLine 欄位
  `
}
```

**關鍵設計**：工具最小化到極致（只給 2 個），任務明確到不需要更多工具。用 `sonnet` 是因為 bash/zsh 語法轉換需要中等推理能力，`haiku` 容易出錯。
