# Vector Memory — Tools Reference

## Core Tools

### memory_recall — Search memories

Hybrid retrieval (vector 0.7 + BM25 0.3) with reranking and decay.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `query` | string | yes | — | Search query (semantic + keyword) |
| `limit` | number | no | 5 | Max results (up to 20) |
| `scope` | string | no | — | Filter by scope |
| `category` | enum | no | — | preference / fact / decision / entity / skill / lesson / other |
| `since` | string | no | — | Time filter: "3d", "1w", "2h", or ISO timestamp |

### memory_store — Save a memory

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `text` | string | yes | — | Memory content (keep < 500 chars) |
| `importance` | number | no | 0.7 | Score 0–1 |
| `category` | enum | no | — | Classification |
| `scope` | string | no | default | Target scope |
| `lesson_trigger` | string | no | — | For `lesson`: what situation triggers this |
| `lesson_rule` | string | no | — | For `lesson`: the rule to follow |
| `lesson_principle` | string | no | — | For `lesson`: the universal principle |

### memory_update — Update a memory

For `preference`/`entity`, text changes create a new version (supersede) preserving history. Metadata-only changes (importance, category) update in-place.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `memoryId` | string | yes | Full UUID or 8+ char prefix |
| `text` | string | no | New content (triggers re-embedding) |
| `importance` | number | no | New score |
| `category` | enum | no | New category |

### memory_forget — Delete a memory

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `memoryId` | string | either | Direct delete by ID |
| `query` | string | either | Search and delete |
| `scope` | string | no | Scope filter |

### memory_merge — Combine two memories

Creates a new merged memory and invalidates both originals.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `primaryId` | string | yes | Base memory ID |
| `secondaryId` | string | yes | Memory to absorb |
| `mergedText` | string | no | Explicit merged text (default: concatenate both) |
| `importance` | number | no | Override (default: max of both) |

### memory_history — Version history

Trace a memory through its supersede/merge chain.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `memoryId` | string | yes | Any memory in the chain |
| `direction` | enum | no | "forward" / "backward" / "both" (default) |
| `scope` | string | no | Scope filter |

---

## Self-Improvement Tools

These are disabled by default. Enable with `MEMORY_ENABLE_SELF_IMPROVEMENT=true`.

### self_improvement_log — Record learning/error

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | enum | yes | `learning` / `error` |
| `summary` | string | yes | One-line summary |
| `details` | string | no | Full details |
| `suggestedAction` | string | no | Prevention measure |
| `category` | string | no | correction / best_practice / knowledge_gap |
| `area` | string | no | frontend / backend / infra / tests / docs / config |
| `priority` | string | no | low / medium / high / critical |

### self_improvement_extract_skill — Create skill from learning

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `learningId` | string | yes | Learning entry ID |
| `skillName` | string | yes | Kebab-case name |
| `outputDir` | string | no | Default: `skills` |

### self_improvement_review — Governance overview

No parameters. Returns pending/high-priority/promoted stats.
