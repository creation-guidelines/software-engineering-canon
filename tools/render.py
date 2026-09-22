#!/usr/bin/env python3
"""render.py - render data/ (DuckDB export) into Markdown pages under docs/.

Output is deterministic (no timestamps) so CI can require `git status` to be clean after rendering.
"""
import os

import duckdb

DATA = os.environ.get("DC_DIR", "data")
DOCS = os.environ.get("DOCS_DIR", "docs")

FORWARD = {"serves": "Serves", "supplies": "Supplies", "enforces": "Enforces",
           "pairs-with": "Pairs with", "same-family-as": "Same family as"}
BACKWARD = {"serves": "Served by", "supplies": "Supplied by", "enforces": "Enforced by",
            "pairs-with": "Pairs with", "same-family-as": "Same family as"}

con = duckdb.connect()
con.execute(f"IMPORT DATABASE '{DATA}'")


def rows(sql, *params):
    return con.execute(sql, list(params)).fetchall()


# id -> (name, page), for cross-links. backlog is included so a relation could link a backlog
# item to a concept (not used yet, but keeps the id namespace and link() correct if one is added).
index = {}
for page in ("principles", "architectures", "practices"):
    for cid, name in rows(f'SELECT id, name FROM {page} ORDER BY rowid'):
        index[cid] = (name, page)
for cid, name in rows('SELECT id, title FROM backlog ORDER BY rowid'):
    index[cid] = (name, "backlog")
for cid, name in rows('SELECT id, title FROM session_log ORDER BY rowid'):
    index[cid] = (name, "session_log")


def link(cid):
    name, page = index[cid]
    return f"[{name}]({page}.md#{cid})"


def related(cid):
    parts = {}

    def add(label, other, note):
        parts.setdefault(label, []).append(link(other) + (f" ({note})" if note else ""))

    for to_id, rel, note in rows("SELECT to_id, relation, note FROM relations WHERE from_id = ? ORDER BY rowid", cid):
        add(FORWARD[rel], to_id, note)
    for from_id, rel, note in rows("SELECT from_id, relation, note FROM relations WHERE to_id = ? ORDER BY rowid", cid):
        add(BACKWARD[rel], from_id, note)
    return [f"{label}\n: " + ", ".join(dict.fromkeys(items)) for label, items in parts.items()]


def cited(cid):
    srcs = rows("""SELECT s.title, s.url FROM concept_sources cs JOIN sources s ON s.id = cs.source_id
                   WHERE cs.concept_id = ? ORDER BY s.rowid""", cid)
    return [("Sources\n: " + ", ".join(f"[{t}]({u})" for t, u in srcs))] if srcs else []


def origin(author, year):
    if not author and not year:
        return []
    return ["Origin\n: " + ", ".join(str(x) for x in (author, year) if x)]


def block(cid, name, paragraphs):
    lines = [f'<a id="{cid}"></a>', f"### {name}", ""]
    for p in paragraphs:
        lines += [p, ""]
    return lines


GENERATED = "<!-- Generated from data/ by tools/render.py. Do not edit by hand. -->"


def write(name, lines):
    os.makedirs(DOCS, exist_ok=True)
    with open(f"{DOCS}/{name}", "w") as f:
        f.write("\n".join([GENERATED, ""] + lines).rstrip("\n") + "\n")


# ---- principles ----
out = ["# Principles", "",
       "Small, sharp rules that hold up across languages and eras, followed by the type-driven techniques that let the compiler enforce them.", ""]
for category, heading in (("core", "Core principles"), ("type-driven", "Type-driven design")):
    out += [f"## {heading}", ""]
    for cid, name, statement, caveat, author, year, aliases in rows(
            "SELECT id, name, statement, caveat, origin_author, origin_year, aliases FROM principles WHERE category = ? ORDER BY rowid", category):
        paras = [statement]
        if aliases:
            paras.append("Also known as\n: " + ", ".join(aliases))
        if caveat:
            paras.append("Watch out\n: " + caveat)
        paras += origin(author, year) + related(cid) + cited(cid)
        out += block(cid, name, paras)
write("principles.md", out)

# ---- architectures ----
out = ["# Architectures", "",
       "Two independent axes: the macro structure of the system (modules and their boundaries) and the micro structure inside a module. Comparing them as rivals is a category error.", ""]
for cid, name, essence, best_when, author, year in rows(
        "SELECT id, name, essence, best_when, origin_author, origin_year FROM architectures ORDER BY rowid"):
    paras = [essence, "Best when\n: " + best_when] + origin(author, year) + related(cid) + cited(cid)
    out += block(cid, name, paras)
write("architectures.md", out)

# ---- practices ----
out = ["# Practices", "", "Habits and tooling that make the principles and architectures stick.", ""]
for cid, name, description in rows("SELECT id, name, description FROM practices ORDER BY rowid"):
    out += block(cid, name, [description] + related(cid) + cited(cid))
write("practices.md", out)

# ---- sources ----
out = ["# Sources", ""]
for sid, title, url, author, year in rows("SELECT id, title, url, author, year FROM sources ORDER BY rowid"):
    by = ", ".join(str(x) for x in (author, year) if x)
    users = [link(c) for (c,) in rows("SELECT concept_id FROM concept_sources WHERE source_id = ? ORDER BY rowid", sid)]
    out.append(f"- [{title}]({url})" + (f", {by}" if by else "") + (f". Cited by: {', '.join(users)}" if users else ""))
write("sources.md", out)

# ---- backlog ----
out = ["# Backlog", "", "Known gaps in this canon, tracked the same way as its content.", ""]
for status, heading in (("open", "Open"), ("in-progress", "In progress"), ("done", "Done")):
    items = rows("SELECT id, title, note FROM backlog WHERE status = ? ORDER BY opened, rowid", status)
    if not items:
        continue
    out += [f"## {heading}", ""]
    for bid, title, note in items:
        out += block(bid, title, [note] if note else [])
write("backlog.md", out)

# ---- session log ----
out = ["# Session Log", "", "One entry per significant decision: what was done, what was considered, what was rejected and why.", ""]
for sid, title, entry_date, done, considered, rejected in rows(
        "SELECT id, title, entry_date, done, considered, rejected FROM session_log ORDER BY entry_date, rowid"):
    paras = ["Date\n: " + str(entry_date), "Done\n: " + done]
    if considered:
        paras.append("Considered\n: " + considered)
    if rejected:
        paras.append("Rejected\n: " + rejected)
    out += block(sid, title, paras)
write("session_log.md", out)

# ---- index ----
counts = {t: rows(f"SELECT count(*) FROM {t}")[0][0] for t in ("principles", "architectures", "practices", "sources", "backlog", "session_log")}
open_backlog = rows("SELECT count(*) FROM backlog WHERE status != 'done'")[0][0]
out = ["# Software engineering canon", "",
       "A curated canon of battle-tested software design principles, type-driven techniques and architectures.",
       "Guiding idea: make the right thing easy and the wrong thing unrepresentable, and prefer structure the compiler and the module boundaries enforce over conventions people must remember.", "",
       f"- [Principles](principles.md): {counts['principles']}",
       f"- [Architectures](architectures.md): {counts['architectures']}",
       f"- [Practices](practices.md): {counts['practices']}",
       f"- [Sources](sources.md): {counts['sources']}",
       f"- [Backlog](backlog.md): {open_backlog} open of {counts['backlog']}",
       f"- [Session Log](session_log.md): {counts['session_log']}", ""]
write("index.md", out)
print("rendered", ", ".join(f"{v} {k}" for k, v in counts.items()))
