# 模型成本對照 + 任務適配

## 價格表（2026-03）

| 模型 | Input/MTok | Output/MTok | Cached Input | 適用 |
|------|-----------|-------------|-------------|------|
| Haiku 3.5 | $0.80 | $4.00 | $0.08 | 搜尋、分類、格式轉換 |
| Sonnet 4.6 | $3.00 | $15.00 | $0.30 | 程式碼分析、中等推理 |
| Opus 4.6 | $15.00 | $75.00 | $1.50 | 深度架構、複雜推理 |
| Opus 4.6 Fast | $30.00 | $150.00 | $3.00 | 需要低延遲的 Opus 任務 |

## Haiku→Opus 成本倍率

| 比較 | Input 倍率 | Output 倍率 |
|------|-----------|-------------|
| Haiku vs Sonnet | 3.75x | 3.75x |
| Haiku vs Opus | 18.75x | 18.75x |
| Haiku vs Opus Fast | **37.5x** | **37.5x** |

## Cached 省多少

Cached input = 原價的 10%。一個 50K token 的 system prompt：
- 首次：$0.15（Sonnet）
- 後續：$0.015（Sonnet cached）
- **省 90%，前提是不 bust cache**
