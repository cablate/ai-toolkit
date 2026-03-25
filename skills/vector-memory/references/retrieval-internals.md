# Vector Memory — Retrieval Internals

Load when debugging retrieval quality. Not needed for daily use.

---

## Hybrid Retrieval Pipeline

```
Query → Vector Embedding + BM25 → RRF Fusion → Rerank → Decay Boost → Length Norm → Filter
```

### Scoring Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| vectorWeight | 0.7 | Semantic relevance weight |
| bm25Weight | 0.3 | Keyword match weight |
| hardMinScore | 0.35 | Minimum score after reranking |
| candidatePoolSize | 20 | Pool size before reranking |

### Post-Retrieval Scoring Stages

1. **Recency Boost** — `exp(-ageDays / halfLife) × weight`
2. **Importance Weighting** — `score × (0.7 + 0.3 × importance)`
3. **Length Normalization** — `1 / (1 + 0.5 × log2(charLen/500))`
4. **Time Decay** — `score *= 0.5 + 0.5 × exp(-ageDays / effectiveHalfLife)`
5. **Cross-Encoder Reranking** — 60% API + 40% original fused
6. **MMR Diversity** — cosine similarity > 0.85 gets downweighted

---

## Weibull Decay Model

Memories automatically decay based on usage frequency and importance.

### Three Tiers

| Tier | Beta | Behavior | Decay Floor |
|------|------|----------|-------------|
| Core | 0.8 | Slow decay | 0.9 |
| Working | 1.0 | Standard exponential | 0.7 |
| Peripheral | 1.3 | Fast decay | 0.5 |

### Promotion / Demotion Rules

- **Peripheral → Working**: access >= 3 AND score >= 0.4
- **Working → Core**: access >= 10 AND score >= 0.7 AND importance >= 0.8
- **Working → Peripheral**: score < 0.15 OR (age > 60 days AND access < 3)
- **Core → Working**: score < 0.15 AND access < 3

### Access Reinforcement

Frequently accessed memories decay slower:
- Only `source: "manual"` accesses count (auto-recall doesn't)
- Logarithmic curve: diminishing returns per access
- Cap: `maxHalfLifeMultiplier = 3`

---

## Default Configuration

- Embedding: DeepInfra + Qwen3-Embedding-8B (1024 dims)
- Reranker: None (vector + BM25 fusion only)
- DB: LanceDB (embedded, per-project or per-agent)
