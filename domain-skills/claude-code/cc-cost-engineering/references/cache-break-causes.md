# Prompt Cache Break 12 原因 + 防禦

| # | 原因 | 可控？ | 防禦方式 |
|---|------|--------|----------|
| 1 | System prompt 文字變化 | 是 | 靜態/動態邊界分離 |
| 2 | Tool schema 變化（數量/描述） | 部分 | 不排序工具陣列、避免動態描述 |
| 3 | MCP 工具動態載入 | 部分 | Deferred loading（ToolSearch） |
| 4 | Agent list inline 變化 | 是 | 改用 attachment 注入（省 10.2%） |
| 5 | `currentDate` 跨日 | **設計缺陷** | 應移到 dynamic zone |
| 6 | Compaction 改寫訊息 | 不可避免 | 用 fork 繼承 cache |
| 7 | Feature flag mid-session 切換 | �� | Sticky Latch（啟用後不關） |
| 8 | Beta header 變化 | 是 | Latch 機制 |
| 9 | 版本更新（tool description 微調） | 不可避免 | — |
| 10 | Permission mode mid-session 切換 | 是 | 避免切換 |
| 11 | Plugin/MCP 重載（`/reload-plugins`） | 是 | 避免使用 |
| 12 | 使用者切換 cwd | 是 | 固定工作目錄 |
