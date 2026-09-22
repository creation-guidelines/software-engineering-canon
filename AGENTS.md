# AGENTS.md - how to work in this repository

This repo is a small versioned "database" of software-engineering knowledge (principles, architectures, practices, sources and the relations between them). The data lives as plain files; SQL edits it; CI enforces that it stays valid and canonical. **Work on the content. Do not re-derive the system.**

## Setup (once per session)
```
make setup    # pins DuckDB (pip) and Miller (mlr); see .tad/bootstrap.sh
make test     # tests for .tad/ itself
make verify   # exactly what CI runs
```

## Layout
| Path | What | Who writes it |
|---|---|---|
| `data/schema.sql` | DDL, one `CREATE` per table | you, by SQL `ALTER` or by hand (see below) |
| `data/load.sql` | `COPY` statements | DuckDB only |
| `data/<table>.json` | one JSON object per line (JSONL despite the extension) | DuckDB only |
| `checks/*.sql` | invariants: each query must return **no rows** | you |
| `docs/*.md` | rendered pages, published to GitHub Pages | `tools/render.py` only |
| `.tad/tools/dc.py` | guard / canonicalize / SQL runner (shared engine, generic) | tooling |
| `tools/render.py` | renderer, specific to this repo's schema - see `.tad/README.md` for why it isn't in `.tad/` | you |

## Rules
1. **Never hand-edit `data/*.json` or `docs/*.md`.** Change data through SQL: `make sql Q="UPDATE ...; SELECT ..."`. Then `make render`.
2. **Always finish with `make canon`** (SQL edits do it automatically). DuckDB must write the final bytes, otherwise CI fails on a non-canonical diff. A plain `mlr` pass rewrites every line with different whitespace.
3. **No BLOB columns.** They corrupt on the first JSON round trip. Use base64 `VARCHAR`.
4. **Do not change DuckDB settings** such as `preserve_insertion_order`; row order is what keeps diffs at one line per changed row.
5. **No foreign keys.** They block nearly every `ALTER TABLE` on the referenced table. Referential integrity lives in `checks/*.sql` instead; add a check whenever you add a relationship.
6. Ids are kebab-case (enforced by CHECK) and share one namespace across `principles`, `architectures`, `practices`.
7. **New or changed factual claims need a source.** Add a row to `sources` (a real URL you actually opened) and link it in `concept_sources`. Do not invent attributions or dates; leave `origin_*` NULL when unsure. `checks/04` fails on a source nobody cites. Note: the initial load came from an unsourced draft, so many older concepts have no source yet; that is backlog, not a licence to add more (list it with the recipe below).
8. One logical change per commit, prefixed `data:`, `schema:`, `tools:` or `docs:`.
9. **Keep `backlog` and `session_log` current.** Every known gap goes in `backlog` (status:
   open/in-progress/done), not a separate tracker or a prose TODO. Every significant decision -
   what was done, what was considered, what was rejected and why - gets a `session_log` row, so
   the reasoning survives past the conversation that produced it. Both render to their own page the
   same as any other content: [`docs/backlog.md`](docs/backlog.md), [`docs/session_log.md`](docs/session_log.md).

## Recipes
Add or change content:
```
make sql Q="INSERT INTO principles VALUES ('id','Name','core','One-line statement.',NULL,NULL,NULL)"
make sql Q="UPDATE principles SET caveat = '...' WHERE id = 'dry'"
make render && make verify
```
Find concepts still missing a source (backlog):
```
make sql Q="SELECT id FROM (SELECT id FROM principles UNION ALL SELECT id FROM architectures UNION ALL SELECT id FROM practices) WHERE id NOT IN (SELECT concept_id FROM concept_sources) ORDER BY id"
```
Schema change, when DuckDB allows it (add column with default, rename column, drop a non-key column, change a non-key type, `SET NOT NULL`, rename table):
```
make sql Q="ALTER TABLE principles ADD COLUMN maturity VARCHAR DEFAULT 'stable'"
```
Schema change DuckDB refuses (add a column with constraints, `ADD CONSTRAINT CHECK`, drop or retype a key column):
```
# 1. edit the CREATE line in data/schema.sql by hand
# 2. give every data line the new key (Miller, in place):
mlr -I --ijsonl --ojsonl put '$weight = 1' data/principles.json
# 3. validate and normalize; a wrong edit fails loudly here and leaves files untouched
make canon && make render && make verify
```
Rename a field across all lines: `mlr -I --ijsonl --ojsonl rename old,new data/<table>.json`, edit the same name in `data/schema.sql`, then `make canon`. Forgetting the schema edit is caught by `make check` (DuckDB itself would silently load NULLs).

## Why it is built this way
- DuckDB is the engine (in memory; no `.db` file is committed). `IMPORT DATABASE` loads `data/`, `EXPORT DATABASE ... (FORMAT json)` writes it back byte-stably.
- `.tad/tools/dc.py check` exists because DuckDB's `COPY FROM json` silently drops unknown keys and NULL-fills missing nullable columns.
- `.tad/` is the shared engine, vendored as a [`git subrepo`](https://github.com/ingydotnet/git-subrepo) from [creation-guidelines/tad-engine](https://github.com/creation-guidelines/tad-engine) (originally extracted from this repo into [creation-guidelines/text-as-data-template](https://github.com/creation-guidelines/text-as-data-template)). Pull engine updates with `git subrepo pull .tad` - conflict-free as long as nothing in `.tad/` is hand-edited here. (Moved here from `git subtree`: one commit per sync instead of two, and `.tad/.gitrepo` states the tracked remote/branch/commit explicitly.)
- `tools/render.py` stays local (not in `.tad/`) because this content's presentation - grouping principles into "Core" and "Type-driven design", "Watch out:" for a caveat, "Also known as:" for aliases, a combined italicized origin line - doesn't fit `.tad/tools/render.py`'s generic conventions (every column as a plain `**Column:** value` line, no grouping). Both read the same `data/` and write to the same `docs/`; only presentation differs. If this content's needs ever simplify to just the generic conventions (a relations table, a sources table), delete this file and call `.tad/tools/render.py` from the Makefile instead.
- Findings and measurements behind these rules are in the design spike: https://github.com/grenudi/design-canon/pull/1
