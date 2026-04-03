# 常見問題與修正模式

8 類反覆出現的配置問題，附通用 before/after 範例與遷移說明。

---

## Issue 1：角色定義寫機制不寫人格

**為何重要**（cc-prompt-craft）
角色定義是模型讀到的第一句話，設定整個對話的語氣基調。機制描述（「透過工具存取記憶」）從工具列表就看得出來，不需要說；人格描述（「不是秘書，是挑剔的同事」）才能真正影響語氣。

**Before**
```
你是一個有記憶、有觀點的 AI 助手。你透過工具系統維持跨 session 的記憶，並能存取外部資源。
```

**After**
```
某某的工作夥伴，不是企業秘書。什麼都會幫忙，但也會吐槽。
```

**Migration**：技術機制說明（「透過工具系統」）直接刪除，無需保存——工具列表本身就是這個資訊。

---

## Issue 2：使用者期待含任務特定指令

**為何重要**（cc-cost-engineering）
CLAUDE.md 的使用者期待出現在每輪對話的 context 裡。「寫文章要有 hook」對聊天完全無用，卻每輪都消耗 token。任務特定指令屬於對應 skill 的 SKILL.md 正文。

**Before**
```markdown
## 使用者期待
- 寫文章/電子報時，開頭要有吸引人的 hook
- 分析任務必須先列出所有假設再進行
- 回覆不要太短，要有足夠解釋
- 不要反問太多
```

**After**
```markdown
## 使用者期待
- 不要反問太多
```

**Migration**
- 「寫文章要有 hook」→ 搬到 writing skill 的 SKILL.md 正文
- 「分析要先列假設」→ 搬到 analysis skill 的 SKILL.md 正文
- 「回覆不要太短」→ 保留（適用所有對話）或移到共用 rules

---

## Issue 3：核心原則與 rules 重複

**為何重要**（cc-prompt-craft）
重複指令不會加強效果，反而讓模型不確定哪個版本 takes priority。rules 通過 @import 或 system-reminder 已注入，CLAUDE.md 再寫一遍是雙重佔用 context。

**Before**（CLAUDE.md 核心原則）
```markdown
- 記憶是輔助，不是真相：context summary 可能過時，以使用者當下說的為準
- Skill 先行：收到任務先看有無對應 skill
- 說找不到之前先搜：不要直接說「找不到」
```

**After**（CLAUDE.md 核心原則）
```markdown
（原則 1、2、3 已由 .claude/rules/agent-behavior.md 涵蓋，移除）
```

**Migration**：確認 `.claude/rules/` 的對應規則已存在後，從 CLAUDE.md 刪除。被刪的原則繼續透過 rules 注入，不是消失。

---

## Issue 4：Skill description 過長

**為何重要**（cc-cost-engineering × agentskill-expertise）
description 出現在每輪 system-reminder。若 10 個 skill 各有 15 行 description，等於每輪多消耗 ~1500 token，完全沒有換到更好的觸發準確度——觸發只需要觸發條件。

**Token 計算範例**
```
Before: 15 行 description × 10 skill = 150 行 ≈ 1500 token/輪
After:  2 句 description × 10 skill  = 20 行  ≈ 200  token/輪
節省: ~1300 token/輪
```

**Before**（某 skill）
```yaml
description: |
  講座與線上課程設計方法論。提供結構設計、認知負荷管理、互動設計。
  ⚠️ 通用原則也可用於工作坊與演講。
  觸發情境：
  - 設計一個主題的講座或課程
  - 審查現有課綱
  - 優化開場或結尾
  主動更新時機：
  - 完成一次課程設計後更新此 skill
  - 發現新的教學模式後記錄
```

**After**
```yaml
description: "講座與課程設計方法論。觸發：設計講座/課綱、審查課程結構、優化開場結尾。"
```

**Migration**：觸發情境細節和更新時機搬到 SKILL.md 正文的對應區段，內容完整保留。

---

## Issue 5：Wildcard + 個別權限並存

**為何重要**（cc-agent-design）
`mcp__tool__*` 已涵蓋該 tool 的所有方法。再列個別方法是冗餘配置，增加 settings 維護負擔，且在某些實作中可能造成優先級混淆。

**Before**
```json
"allowedTools": [
  "mcp__browser__*",
  "mcp__browser__navigate",
  "mcp__browser__click",
  "mcp__browser__fill",
  "mcp__browser__screenshot"
]
```

**After**
```json
"allowedTools": [
  "mcp__browser__*"
]
```

**Migration**：直接刪除個別條目，wildcard 已涵蓋。若需要限制只允許特定方法，改用精確列表（不用 wildcard）。

---

## Issue 6：缺少 frontmatter

**為何重要**（agentskill-expertise）
沒有 frontmatter，Claude Code 無法將此 skill 的 description 注入 system-reminder。等於這個 skill 在 session 中「不存在」，模型不知道要使用它，也無法在觸發情境下自動匹配。

**Before**（SKILL.md 開頭）
```markdown
# My Skill Name

這個 skill 的功能是...
```

**After**
```markdown
---
name: my-skill-name
description: "技能說明。觸發：xxx、yyy、zzz。"
version: 202604
context: fork
---

# My Skill Name

這個 skill 的功能是...
```

**Migration**：無需遷移，這是純補充操作。

---

## Issue 7：Lessons 應畢業未畢業

**為何重要**（cc-prompt-craft）
Lessons Learned 是臨時觀察的暫存區，不是永久規則的家。當一條 Lesson 的核心意圖已被共用 rules 用更正式的方式表達，繼續保留在 CLAUDE.md 是重複且佔用 context 的。

**畢業判斷標準**
- 共用 rules 已有語意相同的規則 → 畢業
- 超過 3 個月未被觸發/更新 → 畢業候選（人工確認）
- Lesson 只針對特定任務場景 → 搬到對應 skill，非「畢業」

**Before**（CLAUDE.md Lessons）
```markdown
## Lessons Learned
- 不要在心裡記觀察，要寫下來
- 說找不到檔案之前先搜一下
- 已有結論的問題不要再問
- 在 Discord channel 發訊息要確認頻道 id 正確
```

**After**
```markdown
## Lessons Learned
- 在 Discord channel 發訊息要確認頻道 id 正確
```

**Migration**
- 前三條 → 確認 `.claude/rules/agent-behavior.md` 已有對應規則後刪除
- 第四條 → 保留（特定於此 agent 的操作場景，尚未通用化）

---

## Issue 8：Description 豐富性 vs. 最小化的矛盾

**為何重要**
`agentskill-expertise` 希望 description 豐富以提高觸發準確度；`cc-cost-engineering` 希望 description 最小以減少 token 消耗。這個矛盾不能靠「折衷」解決，只能靠三層分離原則解決。

**錯誤思路（折衷）**
```yaml
# 企圖在 description 裡放 3 條觸發範例 + 1 句能力概述
description: |
  工具輔助記憶系統。處理向量記憶寫入與查詢。
  觸發：
  - 需要記憶某事時
  - 查找過去的記錄時
```
這樣 description 仍然偏長，兩邊都沒做到。

**正確思路（三層分離）**
```yaml
# Layer 1: description — 只放觸發條件，≤2 句
description: "向量記憶管理。觸發：寫入新記憶、查詢過去記錄、記憶庫維護。"
```
```markdown
# SKILL.md 正文 — Layer 2

## 能力範圍
- 向量相似度查詢
- 分層記憶（短期 / 長期）
- 記憶衝突解決策略

## 使用時機（詳細）
- 使用者說「記住這件事」...
```
```markdown
# references/memory-patterns.md — Layer 3

案例與教訓...
```

**Migration**：description 的詳細觸發案例搬到 SKILL.md 正文的「使用時機」區段；能力說明保持在 SKILL.md 正文；案例和歷史教訓搬到 references/。
