# 12 條 Harness Engineering 設計原則

| # | 原則 | Claude Code 做法 |
|---|------|-----------------|
| 1 | Cache 穩定性即核心資產 | Sticky Latch、確定性 ID、靜態/動態邊界 |
| 2 | 多層防護的工具執行管道 | 7 層管道，每層可拒絕，執行在最後 |
| 3 | 並行安全性由工具聲明 | `isConcurrencySafe` 由工具自己定義 |
| 4 | Async Generator 是 Agent Loop 的自然表達 | `queryModel` 和 `runTools` 都是 async generator |
| 5 | 錯誤分類決定重試策略 | `classifyToolError` 用 minification-safe 的 name 匹配 |
| 6 | Context 是有限資源 | 10 步 `normalizeMessagesForAPI` 管道 |
| 7 | Deferred Loading 減少啟動成本 | ToolSearch 按需載入 tool schema |
| 8 | Forked Agent 共享 Cache | 子 agent 繼承父 session 的 prompt cache |
| 9 | 觀測不應改變被觀測者 | PII 安全型別 + telemetry 不進 context |
| 10 | 事故驅動的常數設計 | 50 條上限（36.8GB）、167K 重試抑制 |
| 11 | Feature Flag 漸進部署 | 82 個 `tengu_*` flag，random word pair 混淆 |
| 12 | 環境偵測優於顯式配置 | Provider 用環境變數偵測，不要求使用者配置 |
