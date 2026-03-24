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
├── agents/
│   ├── dispatch/          # SOP 式 agent，提升 subagent 品質
│   │   ├── analyst.md      # 架構設計 / 實作規劃 / 健康稽核
│   │   ├── investigator.md # 搜尋 / 探索 / 除錯 / 外部調查
│   │   ├── builder.md      # 程式碼實作 / 測試
│   │   ├── reviewer.md     # Code review / 死碼清理
│   │   └── doc-sync.md     # 文件初始化 / 文件同步
│   └── interactive/
│       └── agent-factory.md  # 設計並產生新 agent
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

`/thorough` 分派平行 subagent 時，prompt 品質決定產出品質。Dispatch agents 是為此場景設計的 **SOP 式 prompt** — 基於步驟的工作流程，附帶明確的閾值規則、分類啟發式和結構化輸出格式。當 Claude Code 透過 Agent tool 產生 subagent 時也同樣適用。

| Agent | 模型 | 模式 | 分派時機 |
|-------|------|------|---------|
| [`analyst`](agents/dispatch/analyst.md) | opus | 架構 / 規劃 / 稽核 | 「設計這個」「規劃實作」「稽核 codebase」 |
| [`investigator`](agents/dispatch/investigator.md) | sonnet | 搜尋 / 探索 / 除錯 / 外部 | 「找 X 的所有用法」「這怎麼運作」「為什麼 fail」 |
| [`builder`](agents/dispatch/builder.md) | sonnet | 建立 / 修改 / 測試 | 「實作這個」「改 handler」「幫 X 寫測試」 |
| [`reviewer`](agents/dispatch/reviewer.md) | sonnet | Review / 清理 | 「review 這段 code」「找死碼」「清理 unused exports」 |
| [`doc-sync`](agents/dispatch/doc-sync.md) | sonnet | 初始化 / 同步 | 「建立專案文件」「code 改了同步文件」 |

每個 agent 根據分派 context 自動判斷模式。一個 agent，多個工作流程。

### 設計原則

1. **零概念講解** — 全部是操作指令。Claude 已經知道 CQRS 是什麼。
2. **步驟式 SOP** — 「做 X，然後 Y，若 Z 閾值 → 執行動作」。不是「你是某某專家」。
3. **硬規則 = 閾值 + 觸發** — `>50 行 → flag`、`>4 層巢狀 → flag`。不是「保持函式簡短」。
4. **分類啟發式** — `AUTO-FIX / ASK / CRITICAL` 附帶具體判斷標準。不是勾選清單。
5. **結構化輸出** — 每個 agent 都有 report 模板。一致、可解析。

## 互動式 Agents

| Agent | 說明 |
|-------|------|
| [`agent-factory`](agents/interactive/agent-factory.md) | 設計並產生新 agent——調研最佳實踐、分析需求、輸出可用的 agent prompt |

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

## 授權

[MIT](LICENSE)
