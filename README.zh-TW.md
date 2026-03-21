# Cab 的 Claude Code 設定

[English](README.md)

實戰驗證過的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 設定、Skills 和工具。不是理論——全部從每天跟 AI agent 協作的真實工作流中提煉。

## 內容一覽

### Skills

改變 AI agent 工作方式的斜線指令。

#### `/handoff` — Session 交接

把整段對話的 context 壓縮成結構化 prompt，貼到新 session 就能無縫接續。

- P0/P1 優先級分級——帶走重要的，精簡次要的
- 使用者指示逐字保留（不改寫、不摘要）
- 「共識與認知」section——轉移隱性知識
- 自足性輸出——在任何 AI 環境都能用

→ [`skills/handoff/SKILL.md`](skills/handoff/SKILL.md)

#### `/thorough` — 極致交付模式

高問責執行模式。AI 不再客客氣氣，而是以 owner 身份作業——窮盡一切方案、積極平行處理、驗證完成才收工。

- 三條鐵律：窮盡一切、先做後問、主動出擊
- 壓力升級機制（L1→L4）
- 成本優先模型選擇：haiku（預設）→ sonnet → opus
- 嚴格交付檢查清單，含 build 驗證

→ [`skills/thorough/SKILL.md`](skills/thorough/SKILL.md)

### Statusline

Claude Code 的 PowerShell 狀態列，讓成本和 context 使用一目了然。

- Token 用量精確到 K（input/output/cache）
- Context window 使用率視覺化長條 + 告警門檻
- Session 閒置時長（cache rebuild 風險指標）
- 5 小時 / 7 天方案使用率

→ [`statusline/statusline.ps1`](statusline/statusline.ps1)

**設定：**
```jsonc
// ~/.claude/settings.json
{
  "status_line_command": "powershell -NoProfile -File C:/Users/YOU/.claude/statusline.ps1"
}
```

## 安裝

### Clone + Symlink（推薦）

```bash
git clone https://github.com/cablate/cablate-skills.git

# Skills — Linux / macOS
ln -s "$(pwd)/cablate-skills/skills/handoff" ~/.claude/skills/handoff
ln -s "$(pwd)/cablate-skills/skills/thorough" ~/.claude/skills/thorough

# Skills — Windows（以管理員身份開啟 PowerShell）
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\handoff" -Target ".\cablate-skills\skills\handoff"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\thorough" -Target ".\cablate-skills\skills\thorough"

# Statusline
cp cablate-skills/statusline/statusline.ps1 ~/.claude/
```

### 直接複製

```bash
git clone https://github.com/cablate/cablate-skills.git
cp -r cablate-skills/skills/handoff ~/.claude/skills/
cp -r cablate-skills/skills/thorough ~/.claude/skills/
cp cablate-skills/statusline/statusline.ps1 ~/.claude/
```

## 使用方式

```
/handoff          # 產出 context 交接 prompt
/thorough <任務>  # 以極致交付模式執行任務
```

`/handoff` 也會被自然語言觸發，例如「幫我換 session」、「token 快爆了」。

`/thorough` 可以搭配任何任務——它改變的是 AI *怎麼做*，不是*做什麼*。

## 設計哲學

這裡的每樣東西都來自真實痛點：

1. **AI agent 太容易放棄。** 沒驗證就說「完成了」、建議「使用者手動處理」、把半成品當交付。`/thorough` 解決這個問題。

2. **Session 連續性天生斷裂。** 對話碰到 context 上限，所有隱含理解全部蒸發。`/handoff` 解決這個問題。

3. **你對成本一無所知。** 預設的 Claude Code 不會告訴你 token 燒了多少、方案用量到哪裡。Statusline 解決這個問題。

一個原則：**AI 是 owner，不是助手。**

## 貢獻

歡迎開 Issue 和 PR。如果你有符合同樣哲學的東西——實戰驗證、具體行為改變、不打空話——歡迎提交。

## 授權

[MIT](LICENSE)
