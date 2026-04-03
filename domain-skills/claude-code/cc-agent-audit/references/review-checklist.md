# Review Checklist

審計時逐項過，不要跳。每項標 PASS 或 ISSUE，有 ISSUE 就記錄到報告的 Issues 區段。

---

## Check 1：CLAUDE.md 文本品質

**角色定義**
- [ ] 描述的是人格特質或語氣基調（而非技術機制）？
- [ ] 即使不看其他部分，也能從第一句感受到這個 agent 的風格？

**使用者期待**
- [ ] 每一條都跟「所有對話」相關（而非特定任務）？
- [ ] 沒有寫作格式、分析步驟等任務特定指令？
- [ ] 任務特定的指令已搬到對應的 skill？

**核心原則**
- [ ] 逐條與 `.claude/rules/` 的所有檔案對照，無重複？
- [ ] 無相互矛盾的原則（規則方向一致）？

**結構順序（cache 友善）**
- [ ] 穩定內容（角色定義、原則、使用者期待、路徑表等）在前？穩定區段之間的順序不拘
- [ ] Lessons Learned 在最後？
- [ ] 沒有易變的動態內容（如日期、計數器）夾在穩定內容之間？

**Lessons Learned**
- [ ] 條目總數 ≤ 10？
- [ ] 逐條與 `.claude/rules/` 對照，無被共用規則已涵蓋的？
- [ ] 有長期未觸發的舊 Lesson？（畢業候選。門檻依專案定義，建議 1-6 個月）

**Skill 關鍵字表（若存在）**
- [ ] 表中每個 skill 名稱都有對應的 `SKILL.md` 檔案存在？
- [ ] 沒有引用已刪除或改名的 skill？

---

## Check 2：Skill Description 品質

針對每個 `.claude/skills/*/SKILL.md`：

**Frontmatter**
- [ ] 檔案有 `---` 包圍的 YAML block？
- [ ] block 內有 `name` 欄位？
- [ ] block 內有 `description` 欄位？

**Description 內容**
- [ ] description 不超過 2 句話？
- [ ] 包含觸發條件（「觸發：」或「Use when:」）？
- [ ] 沒有能力列表、更新時機、版本歷史等非觸發資訊？
- [ ] 沒有 emoji 條列（這類內容屬於 SKILL.md 正文）？

**格式一致性（跨所有 skills）**
- [ ] 所有 skills 使用同一種觸發格式（中文「觸發：」或英文「Use when:」）？
- [ ] description 的句式風格一致？

**Token 估算**
- 計算：(精簡前平均長度 - 精簡後平均長度) × skill 數量 = 每輪節省 token

---

## Check 3：Settings 配置

讀取 `settings.local.json`（或 `settings.json`）：

**工具清單**
- [ ] allow list 的每個工具，在這個 agent 的實際工作流程中都會用到？
- [ ] 沒有「以防萬一」加進去的工具？

**權限冗餘**
- [ ] 若有 `mcp__toolname__*` wildcard，該 tool 沒有另外列個別方法？
- [ ] 若有 `Bash` 等通用工具，沒有額外列重複的子權限？

**安全性**
- [ ] agent 若會執行 Bash，有 `deny` 陣列？
- [ ] deny 陣列包含危險指令的保護規則（如進程終止、系統修改）？

**Model 適配**
- [ ] 當前 model 匹配此 agent 的任務複雜度？
- [ ] 簡單重複任務（排程、反思）沒有用高成本 model？

---

## Check 4：Rules 對齊

讀取 `.claude/rules/` 底下的所有檔案：

**無矛盾**
- [ ] rules 的每條指令方向與 CLAUDE.md 一致？
- [ ] 無「rules 說做 X，CLAUDE.md 說不要做 X」的情況？

**無重複**
- [ ] CLAUDE.md 的每條指令，在 rules 裡沒有語意相同的版本？
- [ ] rules 之間互相不重複？

**@import 有效性**
- [ ] 若使用 `@import` 語法，被引用的路徑存在？
- [ ] 被引用的檔案不是空檔案或已廢棄的？

---

## Check 5：跨檔一致性

若無 persona/soul.md → 此 check 標記 N/A，跳過。

**角色定義**
- [ ] CLAUDE.md 的角色描述與 soul.md 的 "Who I Am" 一致（沒有衝突的個性設定）？

**工作原則**
- [ ] CLAUDE.md 核心原則沒有與 soul.md Work Principles 方向相反的條目？

**使用者期待 vs. Quirks**
- [ ] CLAUDE.md 使用者期待的每一條，在 soul.md Quirks 或 How I Sound 裡沒有重複？

---

## 完成標準

所有 check 都標 PASS 或有 ISSUE 記錄後，產出：
1. Summary（5 行，每 check 一行）
2. Issues 清單（含 before/after 和 migration 說明）
3. Token Impact 估算
