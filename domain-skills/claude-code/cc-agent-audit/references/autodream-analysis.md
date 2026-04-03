# Claude Code AutoDream 記憶整合機制

來源：claude-code-source/src/services/autoDream/

## 四階段 Consolidation Prompt

### Phase 1 — Orient
- ls 記憶目錄了解現有結構
- 讀 MEMORY.md 了解索引
- 掃現有 topic 檔避免建重複

### Phase 2 — Gather
- 從日誌（logs/YYYY/MM/YYYY-MM-DD.md）找新 signal
- 從現有記憶找過時/矛盾的事實
- 從 transcript 窄搜特定 context（grep narrow terms，不讀整檔）

### Phase 3 — Consolidate
- 合併新 signal 到現有 topic 檔（不建近似重複）
- 相對日期轉絕對日期
- 刪除矛盾事實——「fix it at the source」

### Phase 4 — Prune & Index
- MEMORY.md ≤200 行 ≤25KB
- 每條 ≤150 字：`- [Title](file.md) — one-line hook`
- 移除過時指標、壓縮冗長條目

## 觸發機制
- 三層閘門（最便宜優先）：時間 ≥24h → session ≥5 → 拿到 consolidation lock
- 10 分鐘 scan 節流防止每 turn 都掃描

## 執行方式
- Forked agent（背景、skipTranscript: true、不進對話紀錄）
- Bash 限唯讀（ls, find, grep, cat, stat, wc, head, tail）
- 用主 session 的模型（不降級）

## 記憶類型
| 類型 | 用途 | 結構 |
|------|------|------|
| user | 使用者角色、偏好、知識 | 自由格式 |
| feedback | 工作指導（避免/保留） | Rule → Why → How to apply |
| project | 進行中工作、決策、事件 | Fact → Why → How to apply |
| reference | 外部系統指標 | 簡潔指標 |

## 什麼不保存
- 可從程式碼推導的（架構、pattern）
- Git 歷史（用 git log）
- 除錯解法（在 commit message）
- CLAUDE.md 已有的
- 瑣碎臨時狀態

## 設計亮點
1. 三層門檻最便宜優先——避免不必要的掃描
2. 「合併到現有 topic 檔而非建新檔」——防止記憶碎片化
3. 矛盾偵測——新事實推翻舊記憶時，在源頭修正
4. 非侵入性——使用者看不到 dream agent 的操作
5. Index 硬限制——防止 MEMORY.md 膨脹
