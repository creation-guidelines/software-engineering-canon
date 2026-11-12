# AGENTS.md - how to work in this repository

This repo is a small versioned "database" of software-engineering knowledge (principles, architectures, practices, sources and the relations between them). The data lives as plain JSON lines, its tables declared in `tables.toml`; [tad](https://github.com/creation-guidelines/tad-engine), a released Rust tool, checks it and keeps it canonical, and CI enforces that it stays valid, canonical and rendered. **Work on the content.**

## Setup (once per session)
```
make setup    # installs tad from its pinned release (its checksum checked)
make verify   # exactly what CI runs
```

## Layout
| Path | What | Who writes it |
|---|---|---|
| `tables.toml` | every table declared as data - fields, types, allowed values, patterns - the rules across tables, and how the pages read | you, by hand (see below) |
| `data/<table>.json` | one JSON object per line (JSONL despite the extension) | `tad` only |
| `docs/*.md` | rendered pages, published to GitHub Pages | `make render` only |

## Rules
1. **Never hand-edit `data/*.json` or `docs/*.md`.** Change a row with `tad set`: it checks the whole repository and keeps nothing that breaks a rule. Then `make render`.
2. **Always finish with `make verify`**: tad must write the final bytes (`tad canon`), or CI fails on a non-canonical diff.
3. **Integrity lives in `tables.toml`**: ids unique across `principles`, `architectures`, `practices`, `backlog` and `session_log` (`unique_ids`), both ends of every relation existing (`references`), every source cited (`appears_in`), no symmetric relation recorded both ways (`no_mirror`). `tad check` runs every rule; add one whenever you add a relationship.
4. Ids are kebab-case (a pattern in `tables.toml`) and share one namespace across the content tables.
5. **New or changed factual claims need a source.** Add a row to `sources` (a real URL you actually opened) and link it in `concept_sources`. Do not invent attributions or dates; leave `origin_*` empty when unsure. A source nobody cites fails `tad check`.
6. One logical change per commit, prefixed `data:`, `schema:`, `tools:` or `docs:`.
7. **Keep `backlog` and `session_log` current.** Every known gap goes in `backlog` (status:
   open/in-progress/done), not a separate tracker or a prose TODO. Every significant decision -
   what was done, what was considered, what was rejected and why - gets a `session_log` row, so
   the reasoning survives past the conversation that produced it. Both render to their own page the
   same as any other content: [`docs/backlog.md`](docs/backlog.md), [`docs/session_log.md`](docs/session_log.md).

## Recipes
Add or change content:
```
tad set principles --key id --set "name=Name" --set category=core --set "statement=One-line statement."
tad set principles --key dry --set "caveat=..."
make render && make verify
```
Find concepts still missing a source (backlog):
```
jq -r .id data/principles.json data/architectures.json data/practices.json | sort > /tmp/concepts
jq -r .concept_id data/concept_sources.json | sort -u > /tmp/cited
comm -23 /tmp/concepts /tmp/cited
```
A new field: declare it in `tables.toml` (a `[[tables.<table>.fields]]` entry with its `name` and `type`, and `required`, `enum` or `pattern` if it has them), then `make canon`: every line gains the field, empty. A required field is then given a value on every row with `tad set` before `make verify` passes.

Rename a field: `mlr -I --ijsonl --ojsonl rename old,new data/<table>.json`, make the same change in `tables.toml` (in the presentation too, if a page shows the field), then `make canon` (forgetting the declaration is caught by `make check`).

Ask the data anything in SQL - joins, counts, what is missing - and change it the same way; a change through SQL is checked exactly as `tad set` is, and kept only if every rule still holds:
```
tad sql "SELECT status, count(*) FROM backlog GROUP BY status"
tad sql "UPDATE backlog SET status = 'done' WHERE id = 'an-id'"
tad sql --file a-query.sql --format csv
```

## Why it is built this way
- The data is plain text in git: one JSON object per line, so a change to one row is a one-line diff, readable without any tool.
- `tables.toml` declares the tables as data (after Frictionless Data's Table Schema): a person reads it, and tad checks every row and every rule across tables against it.
- How the pages read is declared in `tables.toml` too (`[site]` and `[pages.<table>]`): principles grouped into "Core" and "Type-driven design", "Watch out" for a caveat, "Also known as" for aliases, an origin line, relations in words ("Serves", "Served by"), sources as a list. Presentation is data like the rest; this repository needs no renderer of its own.
- tad replaced a vendored Python engine (DuckDB) on 2026-11-11, after giving the same verdicts and the same canonical bytes on this repository and three others; this repository's pages were required to stay byte-identical through the switch, and again when its own renderer retired for declared presentation (only the notice line changed).
- Findings and measurements behind the original rules are in the design spike: https://github.com/grenudi/design-canon/pull/1
