# 17 個 Prompt Engineering 設計模式

來源：Claude Code v2.1.88 `src/constants/prompts.ts`

| # | 模式 | 原始碼引用 |
|---|------|-----------|
| 1 | 工具偏好金字塔 | 「Use Read instead of cat, Edit instead of sed, Grep instead of grep」 |
| 2 | 強制前置條件 | 「You MUST read the file before editing. This tool will error if you did not read first.」 |
| 3 | 輸出效率指令 | 「Go straight to the point. Lead with the answer, not the reasoning. Skip filler words.」 |
| 4 | Git 安全協議 | 「NEVER force push to main/master. NEVER skip hooks (--no-verify). ALWAYS create NEW commits rather than amending.」 |
| 5 | 反覆述禁令 | 「Do not restate what the user said — just do it.」 |
| 6 | 範圍控制 | 「Don't add features beyond what was asked. A bug fix doesn't need surrounding code cleaned up.」 |
| 7 | 可逆性評估 | 「Consider reversibility and blast radius of actions. Measure twice, cut once.」 |
| 8 | 動態 context 注入 | `currentDate`、model name、cwd 在組裝時注入 |
| 9 | 靜態/動態邊界 | `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 分離快取域 |
| 10 | DANGEROUS_ 命名 | `DANGEROUS_uncachedSystemPromptSection` 風險即 API 名稱 |
| 11 | 條件段落 | `feature()` 和 `USER_TYPE` 控制段落出現與否 |
| 12 | Eval 驅動措辭 | MEMORY.md 標題、NO_TOOLS_PREAMBLE 位置都經 A/B 測試 |
| 13 | 三層安全檔案 | `cyberRiskInstruction.ts` 同時對開發者/模型/使用者 |
| 14 | 分眾 prompt | ant vs 外部版的 BashTool、EnterPlanMode prompt 差異 |
| 15 | 工具結果摘要提示 | 「Write down important information — original tool result may be cleared later.」 |
| 16 | Scratchpad 目錄 | 每個 session 的暫存目錄，取代 /tmp |
| 17 | Function Result Clearing | 舊工具結果自動清除，保留最近 N 個 |
