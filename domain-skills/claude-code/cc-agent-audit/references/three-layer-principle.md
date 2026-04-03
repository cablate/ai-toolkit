# 三層分離原則

## 背景：一個真實的矛盾

在設計 skill description 時，兩個原則會正面衝突：

**agentskill-expertise 說**：description 要夠豐富，讓模型能準確判斷「什麼情況下應該載入這個 skill」。觸發準確度越高，skill 越不會被遺漏。

**cc-cost-engineering 說**：description 出現在每輪 system-reminder，所有 skill 的 description 加起來每輪消耗固定 token，無論這個 skill 本輪是否被使用。應該最小化。

這個矛盾不能靠「折衷」解決——縮短 description 會讓觸發變模糊，但保持長 description 每輪都在燒 token。折衷只是兩邊都做差。

**解法是：把不同職責的內容放在不同層，而不是壓縮同一層。**

---

## 三層定義

### Layer 1：description（每輪注入）

**職責**：回答「什麼時候該載入我？」

**規格**
- ≤2 句話
- 必須包含觸發條件（「觸發：」或「Use when:」）
- 禁止放：能力列表、更新政策、版本資訊、詳細範例

**Claude Code 機制**：description 欄位的內容出現在每輪的 system-reminder 中，不管使用者有沒有用到這個 skill。

```yaml
# 正確
description: "向量記憶管理。觸發：寫入新記憶、查詢過去記錄、記憶庫維護。"

# 錯誤——能力細節放進來了
description: |
  向量記憶管理系統，支援短期與長期記憶分層。
  可進行相似度查詢、記憶衝突解決。
  觸發：寫入新記憶、查詢過去記錄。
  更新時機：發現新的記憶模式後。
```

---

### Layer 2：SKILL.md 正文（按需載入）

**職責**：回答「我能做什麼？怎麼做？」

**規格**
- 載入條件：使用者或 Claude 明確呼叫 Skill tool 時
- 可包含：能力範圍、工作流程、品質標準、詳細觸發說明
- 不應包含：大量案例、歷史教訓（這些放 Layer 3）

**Claude Code 機制**：使用者或模型執行 Skill tool 時，SKILL.md 的正文內容才被讀入 context。未被呼叫的 skill 其 SKILL.md 不佔 context。

```markdown
## 能力範圍
- 向量相似度查詢（cosine distance）
- 短期記憶（session 內）與長期記憶（跨 session）分層
- 記憶衝突解決：新資訊優先，但保留舊版本為 archived

## 使用時機（詳細）
- 使用者說「記住這件事」「下次記得 XX」→ 寫入
- 使用者說「你有記得 XX 嗎」→ 查詢
- 記憶庫超過 N 條 → 觸發整理流程
```

---

### Layer 3：references/（深度載入）

**職責**：回答「有什麼案例和教訓？」

**規格**
- 載入條件：需要具體案例、歷史教訓、或知識庫時，由 Claude 主動讀取
- 可包含：實際案例、反模式、歷史錯誤、知識積累
- 不應包含：工作流程（Layer 2）、觸發條件（Layer 1）

**Claude Code 機制**：references/ 的檔案是普通 markdown 檔，不自動載入。需要時透過 Read 工具或 @file 語法讀入。

```markdown
# references/memory-patterns.md

## 已知反模式
- 記憶過於細碎：把「今天天氣很好」這類無意義的對話寫入記憶庫
  → 教訓：寫入前判斷「這個資訊 30 天後還有用嗎？」

## 案例：衝突解決
- 2024-03 使用者說「我住台北」，2024-06 說「我搬到台中了」
  → 兩筆都保留，新的標 active，舊的標 archived
```

---

## 層級判斷速查

| 內容類型 | 應在哪層 |
|---------|---------|
| 觸發關鍵字 | Layer 1 description |
| 觸發的邊界條件（詳細） | Layer 2 SKILL.md 正文 |
| 能力列表 | Layer 2 SKILL.md 正文 |
| 工作流程步驟 | Layer 2 SKILL.md 正文 |
| 品質標準 | Layer 2 SKILL.md 正文 |
| 更新政策 | Layer 2 SKILL.md 正文 |
| 版本歷史 | Layer 2 SKILL.md 正文（或 references/） |
| 具體案例 | Layer 3 references/ |
| 已知反模式 | Layer 3 references/ |
| 歷史教訓 | Layer 3 references/ |
| 知識庫、術語表 | Layer 3 references/ |

---

## Token 效益計算

以 10 個 skill 的典型專案為例：

**Before（未分層）**
```
每個 skill description 約 200 token（含能力說明 + 詳細觸發 + 更新政策）
10 個 skill = 2000 token/輪
這 2000 token 中，實際有用的觸發資訊約 50 token/skill = 500 token
浪費：1500 token/輪
```

**After（三層分離）**
```
每個 skill description 約 30 token（純觸發條件）
10 個 skill = 300 token/輪
每輪節省：~1700 token
按每輪 $0.003 估算 → 每 1000 輪節省 $5.10
```

被移走的 1700 token 內容沒有消失——它在 SKILL.md 正文和 references/ 裡。只有在需要時才載入，不用的輪次不消耗。

---

## 常見誤解

**「description 短了，觸發準確度會下降？」**

不會，只要 description 包含正確的觸發關鍵字。觸發判斷依賴的是關鍵字匹配，不是說明的長度。「觸發：寫入記憶、查詢記錄」已足夠讓模型判斷觸發時機。

**「能力說明放在 SKILL.md 正文，模型不會看到，沒用？」**

模型在決定「要不要載入這個 skill」時看 description（Layer 1）。模型在「載入後如何使用這個 skill」時看 SKILL.md 正文（Layer 2）。這是兩個不同的問題，各自在正確的層處理。

**「三層很麻煩，維護成本高？」**

新內容預設放 Layer 2（SKILL.md 正文），累積到有價值後再整理進 Layer 3（references/）。description 只在初次建立時寫好觸發條件，通常不需要頻繁更新。維護成本主要集中在 Layer 2。
