<p align="center">
  <img src="assets/banner.svg" alt="AI Toolkit" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a>
</p>

實戰驗證過的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 設定、Skills 和工具。不是理論——全部從每天跟 AI agent 協作的真實工作流中提煉。

## Skills

| Skill | 說明 |
|-------|------|
| [`/handoff`](skills/handoff/SKILL.md) | Session 交接——壓縮 context 成結構化 prompt，無縫接續新 session |
| [`/thorough`](skills/thorough/SKILL.md) | 極致交付模式——窮盡一切方案、成本優先選模型、驗證完成才收工 |
| [`/agentskill-expertise`](skills/agentskill-expertise/SKILL.md) | Agent Skill 設計知識庫——底層機制、設計哲學、架構模式、常見誤區 |
| [`/collaboration-style`](skills/collaboration-style/skill.md) | AI-人類協作規範——摩擦案例、程式風格偏好、行為準則 |
| [`/self-growth`](skills/self-growth/SKILL.md) | 持續學習框架——從工作中學習、組織知識、建立回饋迴路 |
| [`/method-code-review`](skills/method-code-review/SKILL.md) | Code Review 方法論——追蹤實際使用路徑，而非假設 |
| [`/brainstorming`](skills/brainstorming/SKILL.md) | 結構化腦力激盪——透過協作對話將想法轉化為驗證過的設計 |
| [`/backend-patterns`](skills/backend-patterns/SKILL.md) | 後端開發模式與慣例 |
| [`/frontend-patterns`](skills/frontend-patterns/SKILL.md) | 前端開發模式與慣例 |
| [`/frontend-design`](skills/frontend-design/SKILL.md) | 前端設計原則與 UI 指南 |
| [`/coding-standards`](skills/coding-standards/SKILL.md) | 程式碼品質標準與風格規範 |
| [`/tdd-workflow`](skills/tdd-workflow/SKILL.md) | 測試驅動開發工作流 |
| [`/agentic-mcp`](skills/agentic-mcp/SKILL.md) | MCP Server 設定與模式 |

## Statusline

Claude Code 的成本與 context 監控。Token 用量（K 精度）、context 使用率長條、閒置時長、方案使用率。

→ [`statusline/statusline.ps1`](statusline/statusline.ps1)

```jsonc
// ~/.claude/settings.json
{ "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1" }
```

## 安裝

### Symlink（推薦）

```bash
git clone https://github.com/cablate/ai-toolkit.git
cd ai-toolkit

# 一次 symlink 所有 skill — Linux / macOS
for skill in skills/*/; do
  name=$(basename "$skill")
  ln -sf "$(pwd)/$skill" ~/.claude/skills/"$name"
done

# 一次 symlink 所有 skill — Windows（管理員 PowerShell）
Get-ChildItem -Directory skills | ForEach-Object {
  New-Item -ItemType SymbolicLink -Force `
    -Path "$env:USERPROFILE\.claude\skills\$($_.Name)" `
    -Target "$PWD\skills\$($_.Name)"
}

# Statusline
cp statusline/statusline.ps1 ~/.claude/
```

### 直接複製

```bash
git clone https://github.com/cablate/ai-toolkit.git
cp -r ai-toolkit/skills/* ~/.claude/skills/
cp ai-toolkit/statusline/statusline.ps1 ~/.claude/
```

### 保持同步

用 symlink 的話，`git pull` 就自動更新。用複製的話，pull 後重新執行複製指令。

## 設計哲學

一個原則：**AI 是 owner，不是助手。**

1. **AI agent 太容易放棄。** `/thorough` 解決這個問題。
2. **Session 連續性天生斷裂。** `/handoff` 解決這個問題。
3. **你對成本一無所知。** Statusline 解決這個問題。

## 貢獻

歡迎開 Issue 和 PR。實戰驗證、具體行為改變、不打空話。

## 授權

[MIT](LICENSE)
