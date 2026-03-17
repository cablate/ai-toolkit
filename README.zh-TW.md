# Claude Code Skills

[English](README.md)

一組實戰驗證過的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skills，專門用來逼 AI agent 交出更高品質的端到端成果。

## Skills 一覽

### `/handoff` — Session 交接

把整段對話的 context 壓縮成一段結構化 prompt，貼到新 session 就能無縫接續——不丟關鍵決策、不丟使用者指示、不丟隱性共識。

**核心特性：**
- P0/P1 優先級分級 — 帶走重要的，精簡次要的
- 使用者指示逐字保留（不改寫、不摘要）
- 「共識與認知」section — 轉移對話中建立的隱性知識
- 多工作流支援，適應複雜 session
- 自足性輸出 — 在任何 AI 環境都能用，不只 Claude Code

→ [`skills/handoff/SKILL.md`](skills/handoff/SKILL.md)

### `/thorough` — 極致交付模式

啟動高問責執行模式。AI 不再客客氣氣，而是以 owner 身份作業——窮盡一切方案、積極平行處理、驗證完成才收工。

**核心特性：**
- 三條鐵律：窮盡一切、先做後問、主動出擊
- 壓力升級機制（L1→L4），每級附帶強制動作
- 5 步除錯法，專治「原地打轉」
- 平行處理 + 依複雜度選用模型
- 嚴格交付檢查清單，含 build 驗證

→ [`skills/thorough/SKILL.md`](skills/thorough/SKILL.md)

## 安裝

### 方式一：Symlink（推薦）

Clone 這個 repo，然後 symlink 到 Claude Code 的 skills 目錄：

```bash
git clone https://github.com/cablate/cablate-skills.git

# Linux / macOS
ln -s "$(pwd)/cablate-skills/skills/handoff" ~/.claude/skills/handoff
ln -s "$(pwd)/cablate-skills/skills/thorough" ~/.claude/skills/thorough

# Windows (以管理員身份開啟 PowerShell)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\handoff" -Target ".\cablate-skills\skills\handoff"
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\thorough" -Target ".\cablate-skills\skills\thorough"
```

### 方式二：直接複製

```bash
git clone https://github.com/cablate/cablate-skills.git
cp -r cablate-skills/skills/handoff ~/.claude/skills/
cp -r cablate-skills/skills/thorough ~/.claude/skills/
```

## 使用方式

在任何 Claude Code session 中：

```
/handoff          # 產出 context 交接 prompt
/thorough <任務>  # 以極致交付模式執行任務
```

`/handoff` 也會被自然語言觸發，例如「幫我換 session」、「context 太長了」、「token 快爆了」。

`/thorough` 可以搭配任何任務使用——它改變的是 AI *怎麼做*，不是*做什麼*。

## 設計哲學

這些 Skills 有明確立場。它們存在是因為：

1. **AI agent 太容易放棄。** 沒驗證就說「完成了」、建議「使用者手動處理」、把半成品當交付。`/thorough` 解決這個問題。

2. **Session 連續性天生就是斷裂的。** 對話碰到 context 上限時，所有隱含理解、使用者修正、決策歷史全部蒸發。`/handoff` 解決這個問題。

兩個 Skills 的設計原則只有一個：**AI 是 owner，不是助手。** Owner 不會停在「差不多」。Owner 換班時不會弄丟 context。

## 貢獻

歡迎開 Issue 和 PR。如果你有符合同樣哲學的 Skill——高問責、具體行為改變、不打空話——歡迎提交。

## 授權

[MIT](LICENSE)
