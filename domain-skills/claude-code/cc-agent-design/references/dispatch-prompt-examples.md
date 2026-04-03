# Dispatch Prompt 範例

來源：`src/tools/AgentTool/prompt.ts` — "Writing the prompt" section

---

## 核心原則（原文）

> Brief the agent like a smart colleague who just walked into the room — it hasn't seen this conversation, doesn't know what you've tried, doesn't understand why this task matters.

> **Never delegate understanding.** Don't write "based on your findings, fix the bug" or "based on the research, implement it." Those phrases push synthesis onto the agent instead of doing it yourself. Write prompts that prove you understood: include file paths, line numbers, what specifically to change.

> Terse command-style prompts produce shallow, generic work.

---

## 好的 dispatch — Fork（開放式調查）

```
Audit what's left before this branch can ship. Check: uncommitted changes,
commits ahead of main, whether tests exist, whether the GrowthBook gate is
wired up, whether CI-relevant files changed. Report a punch list — done vs.
missing. Under 200 words.
```

**為什麼好**：
- 明確列出檢查項目（不是「去看看哪裡有問題」）
- 限定輸出格式（punch list，done vs. missing）
- 限定輸出長度（under 200 words）

---

## 好的 dispatch — Subagent（帶完整 context）

```
Review migration 0042_user_schema.sql for safety. Context: we're adding a
NOT NULL column to a 50M-row table. Existing rows get a backfill default.
I want a second opinion on whether the backfill approach is safe under
concurrent writes — I've checked locking behavior but want independent
verification. Report: is this safe, and if not, what specifically breaks?
```

**為什麼好**：
- 說明了背景（50M-row table，NOT NULL column）
- 說明了已知資訊（已查過 locking behavior）
- 說明了需要什麼判斷（concurrent writes 的安全性）
- 要求明確格式（safe/not safe + 具體原因）

---

## 壞的 dispatch（AgentTool prompt 明確列舉的反例）

```
Based on your findings, fix the bug.
```
問題：委外理解。Dispatcher 自己沒有消化研究結論，就推給 agent 做合成。

```
Based on the research, implement it.
```
問題：同上。沒有 file paths、line numbers、具體要改什麼。

```
去檢查這個 migration 有沒有問題。
```
問題：Terse command-style。Agent 不知道背景、不知道你已經查了什麼、不知道具體關注點。

---

## Fork vs Subagent 選擇

| 場景 | 選擇 | 原因 |
|---|---|---|
| 開放式研究問題 | Fork（省略 subagent_type） | 繼承 context，共享 prompt cache |
| 需要獨立觀點（不受父 context 污染） | Subagent（指定 type） | 從零開始，給完整任務描述 |
| 多個獨立子問題 | 多個 Fork 平行 | 一條訊息多個 tool call |
| 實作工作（多檔編輯） | Fork | 中間 tool output 不佔父 context |

**Fork 的特殊規則**（來自 prompt.ts）：
- Fork prompt 是 directive（做什麼），不是 briefing（情況是什麼）。父 context 已繼承。
- 不要 peek：不要 Read/tail output_file，等 completion notification。
- 不要 race：fork 結束前不要猜測結果。用戶問進度 → 回「還在跑」，不要編造結果。

---

## 長度指導

- **研究 fork**：directive 即可，~3-5 行
- **獨立 subagent**：完整 briefing，~8-15 行，含背景 + 已知 + 需要什麼判斷
- **verification agent**：必須包含「原始任務描述」「改了哪些檔案」「採用的方法」
- **Explore agent**：在 prompt 裡指定 thoroughness level：`quick` / `medium` / `very thorough`
