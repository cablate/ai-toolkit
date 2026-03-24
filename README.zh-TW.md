<p align="center">
  <img src="assets/banner.svg" alt="AI Toolkit" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a>
</p>

一整套 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 工作環境。Skills、Dispatch Agents、互動式 Agents、Statusline——全部從每天跟 AI agent 協作的真實工作流中提煉。

## 內容總覽

```
ai-toolkit/
├── agents/
│   ├── dispatch/          # SOP 式 agent，提升 subagent 品質
│   │   ├── analyst.md     # 架構設計 / 實作規劃 / 健康稽核
│   │   ├── reviewer.md    # Code review / 死碼清理
│   │   └── doc-sync.md    # 文件初始化 / 文件同步
│   └── interactive/       # 15 個獨立互動式 agent
│       ├── agent-factory.md
│       ├── consultation-prep.md
│       ├── cinematic-writing-agent.txt
│       └── ... (共 15 個)
├── skills/
│   ├── handoff/           # Session 交接
│   ├── thorough/          # 極致交付模式
│   ├── project-docs/      # 專案文件結構模板
│   ├── agentskill-expertise/
│   ├── collaboration-style/
│   └── self-growth/
└── statusline/            # 成本與 context 監控
```

## Dispatch Agents

Claude Code 產生 subagent（透過 Agent tool 或 `/thorough`）時，prompt 品質決定產出品質。Dispatch agents 是 **SOP 式 prompt** — 基於步驟的工作流程，附帶明確的閾值規則、分類啟發式和結構化輸出格式。沒有角色定義，沒有概念講解。

| Agent | 模型 | 模式 | 分派時機 |
|-------|------|------|---------|
| [`analyst`](agents/dispatch/analyst.md) | opus | 架構 / 規劃 / 稽核 | 「設計這個」「規劃實作」「稽核 codebase」 |
| [`reviewer`](agents/dispatch/reviewer.md) | sonnet | Review / 清理 | 「review 這段 code」「找死碼」「清理 unused exports」 |
| [`doc-sync`](agents/dispatch/doc-sync.md) | sonnet | 初始化 / 同步 | 「建立專案文件」「code 改了同步文件」 |

每個 agent 根據分派 context 自動判斷模式。一個 agent，多個工作流程。

### 設計原則

這些 prompt 遵循嚴格的 SOP 模式（參考 [gstack](https://github.com/garrytan/gstack)）：

1. **零概念講解** — 全部是操作指令。Claude 已經知道 CQRS 是什麼。
2. **步驟式 SOP** — 「做 X，然後 Y，若 Z 閾值 → 執行動作」。不是「你是某某專家」。
3. **硬規則 = 閾值 + 觸發** — `>50 行 → flag`、`>4 層巢狀 → flag`。不是「保持函式簡短」。
4. **分類啟發式** — `AUTO-FIX / ASK / CRITICAL` 附帶具體判斷標準。不是勾選清單。
5. **結構化輸出** — 每個 agent 都有 report 模板。一致、可解析。

## 互動式 Agents

獨立功能的 agent，放進 `~/.claude/agents/` 直接使用。

| Agent | 說明 |
|-------|------|
| [`agent-factory`](agents/interactive/agent-factory.md) | 設計並產生新 agent |
| [`consultation-prep`](agents/interactive/consultation-prep.md) | 諮詢準備 |
| [`srt-subtitle-editor`](agents/interactive/srt-subtitle-editor.md) | SRT 字幕編輯 |
| [`cinematic-writing-agent`](agents/interactive/cinematic-writing-agent.txt) | 電影感敘事寫作 |
| [`design-pattern-coach`](agents/interactive/design-pattern-coach.md) | 設計模式指導 |
| [`reading-agent`](agents/interactive/reading-agent.md) | 結構化閱讀輔助 |
| [`uiux-designer`](agents/interactive/uiux-designer.md) | UI/UX 設計 |
| [`user-value-prd-reviewer`](agents/interactive/user-value-prd-reviewer.md) | 從使用者價值角度審查 PRD |
| [`CodeMender`](agents/interactive/CodeMender.md) | 程式碼修復 |
| [`code-review-agent-v2`](agents/interactive/code-review-agent-v2.md) | Code review |
| [`development-agent`](agents/interactive/development-agent.md) | 開發工作流 |
| [`planning-agent`](agents/interactive/planning-agent.md) | 專案規劃 |
| [`security-helper`](agents/interactive/security-helper.md) | 安全分析 |
| [`ai-quick-start-record-agent`](agents/interactive/ai-quick-start-record-agent.md) | 快速上手文件產出 |

## Skills

| Skill | 說明 |
|-------|------|
| [`/handoff`](skills/handoff/SKILL.md) | Session 交接——壓縮 context 成結構化 prompt，無縫接續新 session |
| [`/thorough`](skills/thorough/SKILL.md) | 極致交付模式——窮盡一切方案、成本優先選模型、驗證完成才收工 |
| [`/project-docs`](skills/project-docs/SKILL.md) | 專案文件結構——標準 `proj-[name]/` 佈局，含 ADR、功能故事、操作指南 |
| [`/agentskill-expertise`](skills/agentskill-expertise/SKILL.md) | Agent Skill 設計知識庫——底層機制、設計哲學、架構模式、常見誤區 |
| [`/collaboration-style`](skills/collaboration-style/skill.md) | AI-人類協作規範——摩擦案例、程式風格偏好、行為準則 |
| [`/self-growth`](skills/self-growth/SKILL.md) | 持續學習框架——從工作中學習、組織知識、建立回饋迴路 |

## Statusline

Claude Code 的成本與 context 監控。Token 用量（K 精度）、context 使用率長條、閒置時長、方案使用率。

> [`statusline/statusline.ps1`](statusline/statusline.ps1)

```jsonc
// ~/.claude/settings.json
{ "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1" }
```

## 安裝

```bash
git clone https://github.com/cablate/ai-toolkit.git
cd ai-toolkit
```

### Linux / macOS

```bash
# Skills
for skill in skills/*/; do
  name=$(basename "$skill")
  ln -sf "$(pwd)/$skill" ~/.claude/skills/"$name"
done

# Dispatch agents
mkdir -p ~/.claude/agents
for agent in agents/dispatch/*.md; do
  ln -sf "$(pwd)/$agent" ~/.claude/agents/$(basename "$agent")
done

# 互動式 agents（挑你需要的）
for agent in agents/interactive/*; do
  ln -sf "$(pwd)/$agent" ~/.claude/agents/$(basename "$agent")
done

# Statusline
cp statusline/statusline.ps1 ~/.claude/
```

### Windows（管理員 PowerShell）

```powershell
# Skills
Get-ChildItem -Directory skills | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\skills\$($_.Name)" `
    -Target "$PWD\skills\$($_.Name)"
}

# Dispatch agents
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\agents"
Get-ChildItem agents\dispatch\*.md | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\agents\$($_.Name)" `
    -Target "$PWD\agents\dispatch\$($_.Name)"
}

# 互動式 agents（挑你需要的）
Get-ChildItem agents\interactive\* | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\agents\$($_.Name)" `
    -Target "$PWD\agents\interactive\$($_.Name)"
}

# Statusline
Copy-Item statusline\statusline.ps1 ~\.claude\
```

### 保持同步

用 symlink 的話，`git pull` 就自動更新。用複製的話，pull 後重新執行複製指令。

## 設計哲學

**AI 是 owner，不是助手。**

1. **AI agent 太容易放棄。** `/thorough` 解決——壓力升級、強制重試、沒有逃生口。
2. **Subagent 品質不穩定。** Dispatch agents 解決——SOP prompt 附帶硬規則，不是模糊的角色描述。
3. **Session 連續性天生斷裂。** `/handoff` 解決——結構化 context 壓縮。
4. **你對成本一無所知。** Statusline 解決——即時 token 與 context 監控。
5. **專案文件會腐爛。** `/project-docs` + `doc-sync` 解決——標準結構加自動偵測過期。

## 貢獻

歡迎開 Issue 和 PR。實戰驗證、具體行為改變、不打空話。

## 授權

[MIT](LICENSE)
