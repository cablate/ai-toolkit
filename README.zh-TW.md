<p align="center">
  <img src="assets/banner.svg" alt="AI Toolkit" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a>
</p>

一整套 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 工作環境。Dispatch Agents、Skills、Statusline——全部從每天跟 AI agent 協作的真實工作流中提煉。

## 內容總覽

```
ai-toolkit/
├── agents/                  # SOP 式 agent（symlink 到 ~/.claude/agents/）
│   ├── analyst.md           # 架構設計 / 實作規劃 / 健康稽核
│   ├── investigator.md      # 搜尋 / 探索 / 除錯 / 外部調查
│   ├── builder.md           # 程式碼實作 / 測試
│   ├── reviewer.md          # Code review / 死碼清理
│   ├── doc-sync.md          # 文件初始化 / 文件同步
│   └── agent-factory.md     # 設計並產生新 agent
├── skills/                  # Skills（symlink 到 ~/.claude/skills/）
│   ├── handoff/             # Session 交接
│   ├── thorough/            # 極致交付模式
│   ├── vector-memory/       # 持久化向量記憶使用指南
│   ├── project-docs/        # 專案文件結構模板
│   ├── agentskill-expertise/ # Skill 設計知識庫
│   ├── collaboration-style/ # AI-人類協作框架
│   └── self-growth/         # 持續學習框架
├── mcp.example.json         # MCP server 設定範本
└── statusline/              # 成本與 context 監控
```

## Agents

Claude Code Agent tool 的 SOP 式 prompt。當 `/thorough` 分派平行 subagent 時，prompt 品質決定產出品質——這些 agent 提供基於步驟的工作流程，附帶明確的閾值規則、分類啟發式和結構化輸出格式。

| Agent | 模型 | 使用時機 |
|-------|------|---------|
| [`analyst`](agents/analyst.md) | opus | 「設計這個」「規劃實作」「稽核 codebase」 |
| [`investigator`](agents/investigator.md) | sonnet | 「找 X 的所有用法」「這怎麼運作」「為什麼 fail」 |
| [`builder`](agents/builder.md) | sonnet | 「實作這個」「改 handler」「幫 X 寫測試」 |
| [`reviewer`](agents/reviewer.md) | sonnet | 「review 這段 code」「找死碼」「清理 unused exports」 |
| [`doc-sync`](agents/doc-sync.md) | sonnet | 「建立專案文件」「code 改了同步文件」 |
| [`agent-factory`](agents/agent-factory.md) | opus | 「建新 agent」「改善這個 agent 的 prompt」 |

每個 agent 根據分派 context 自動判斷模式。一個 agent，多個工作流程。

### 設計原則

1. **零概念講解** — 全部是操作指令。Claude 已經知道 CQRS 是什麼。
2. **步驟式 SOP** — 「做 X，然後 Y，若 Z 閾值 → 執行動作」。不是「你是某某專家」。
3. **硬規則 = 閾值 + 觸發** — `>50 行 → flag`、`>4 層巢狀 → flag`。不是「保持函式簡短」。
4. **分類啟發式** — `AUTO-FIX / ASK / CRITICAL` 附帶具體判斷標準。不是勾選清單。
5. **結構化輸出** — 每個 agent 都有 report 模板。一致、可解析。

## Skills

| Skill | 說明 |
|-------|------|
| [`/handoff`](skills/handoff/SKILL.md) | Session 交接——壓縮 context 成結構化 prompt，無縫接續新 session |
| [`/thorough`](skills/thorough/SKILL.md) | 極致交付模式——窮盡一切方案、成本優先選模型、驗證完成才收工 |
| [`/vector-memory`](skills/vector-memory/SKILL.md) | 持久化向量記憶（LanceDB）——跨 session 儲存事實、決策、教訓 |
| [`/project-docs`](skills/project-docs/SKILL.md) | 專案文件結構——標準 `proj-[name]/` 佈局，含 ADR、功能故事、操作指南 |
| [`/agentskill-expertise`](skills/agentskill-expertise/SKILL.md) | Agent Skill 設計知識庫——底層機制、設計哲學、架構模式、常見誤區 |
| [`/collaboration-style`](skills/collaboration-style/skill.md) | AI-人類協作規範——摩擦案例、程式風格偏好、行為準則 |
| [`/self-growth`](skills/self-growth/SKILL.md) | 持續學習框架——從工作中學習、組織知識、建立回饋迴路 |

## MCP Servers

本 toolkit 使用的 MCP server 設定範本。

> [`mcp.example.json`](mcp.example.json) — 複製到專案目錄改名為 `.mcp.json`，填入你的 API key。

| Server | 用途 |
|--------|------|
| [`@cablate/memory-lancedb-mcp`](https://www.npmjs.com/package/@cablate/memory-lancedb-mcp) | 持久化向量記憶，支援混合搜尋（語意 + 關鍵字） |
| [Serena](https://github.com/oraios/serena) | 語意化程式碼智能——symbol 搜尋、引用追蹤、重構 |

## Statusline

Claude Code 的成本與 context 監控。兩行顯示，附帶 context 警示與方案用量追蹤。

```
 正常（< 60% context）：
┌──────────────────────────────────────────────────────────────────┐
│ Claude Opus 4  | [=======--------------] 45.2K/200.0K 22.6%    │
│ 5h: 12.3% (4h 22m) | 7d: 8.1% (6d 3h)                        │
└──────────────────────────────────────────────────────────────────┘

 警告（>= 60% context）：
┌──────────────────────────────────────────────────────────────────┐
│ Claude Sonnet 4 | concise | [============--------] 130.5K/200.0K 65.3%  /handoff soon │
│ 5h: 45.0% (2h 10m) | 7d: 22.4% (5d 1h)                       │
└──────────────────────────────────────────────────────────────────┘

 危險（>= 80% context）：
┌──────────────────────────────────────────────────────────────────┐
│ Claude Opus 4  | [==================--] 310.0K/200.0K 95.0%  !! HANDOFF NOW !! │
│ 5h: 78.2% (1h 05m) | 7d: 51.3% (3d 12h)                      │
│ !! DO NOT close/resume -- use /handoff first, or waste 6%+ of 5h tokens !! │
└──────────────────────────────────────────────────────────────────┘
```

**第一行** — 模型名稱、輸出風格（非預設時顯示）、context 進度條（K 精度 token 數）、使用率 %，以及 150K/200K/300K 門檻的警示。

**第二行** — 5 小時與 7 天方案使用率，附重置倒數。資料來自 Claude API（快取 5 分鐘）或內建 `rate_limits`（v2.1.80+）。

**第三行** — 250K+ token 時出現。強制警告不要在未 handoff 的情況下關閉或 resume。

> [`statusline/statusline.ps1`](statusline/statusline.ps1)

```jsonc
// ~/.claude/settings.json
{ "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1" }
```

## 授權

[MIT](LICENSE)
