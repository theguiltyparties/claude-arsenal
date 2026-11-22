#!/usr/bin/env python3
"""Search the public-apis catalog (github.com/public-apis/public-apis).

Standard library only. Examples:
  search_apis.py weather
  search_apis.py "stock prices" --no-auth --https
  search_apis.py --category "Music"
  search_apis.py --list-categories
  search_apis.py --refresh            # rebuild the catalog from the live list
"""
import argparse, csv, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(HERE, "..", "data", "apis.tsv")
SOURCE = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
FIELDS = ["category", "name", "url", "description", "auth", "https", "cors"]
ROW = re.compile(r"^\|\s*\[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)\s*\|(?P<rest>.*)\|\s*$")


def parse(md):
    rows, category, in_index = [], None, False
    for line in md.splitlines():
        if line.startswith("### "):
            category = line[4:].strip()
            continue
        m = ROW.match(line)
        if not (m and category):
            continue
        cells = [c.strip() for c in m.group("rest").split("|")]
        if len(cells) != 4:  # skip sponsor tables; the catalog has Description|Auth|HTTPS|CORS
            continue
        desc, auth, https, cors = cells
        auth = auth.strip("`") or "No"
        rows.append([category, m.group("name"), m.group("url"), desc, auth, https, cors])
    return rows


def refresh():
    with urllib.request.urlopen(SOURCE, timeout=30) as r:
        rows = parse(r.read().decode("utf-8"))
    if len(rows) < 500:
        sys.exit(f"Refusing to overwrite: only parsed {len(rows)} APIs from {SOURCE}")
    with open(CATALOG, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(FIELDS)
        w.writerows(rows)
    print(f"Catalog refreshed: {len(rows)} APIs")


def load():
    with open(CATALOG, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("query", nargs="*", help="keywords; every word must match name, description or category")
    p.add_argument("--category", help="substring of the category name, e.g. 'Finance'")
    p.add_argument("--no-auth", action="store_true", help="only APIs that need no key")
    p.add_argument("--https", action="store_true", help="only HTTPS APIs")
    p.add_argument("--cors", action="store_true", help="only APIs with CORS enabled (callable from a browser)")
    p.add_argument("--limit", type=int, default=25)
    p.add_argument("--list-categories", action="store_true")
    p.add_argument("--refresh", action="store_true", help="download the latest list and rebuild the catalog")
    a = p.parse_args()

    if a.refresh:
        refresh()
        return
    rows = load()
    if a.list_categories:
        counts = {}
        for r in rows:
            counts[r["category"]] = counts.get(r["category"], 0) + 1
        for c in sorted(counts):
            print(f"{c} ({counts[c]})")
        return

    words = [w.lower() for w in a.query]
    hits = []
    for r in rows:
        hay = f"{r['name']} {r['description']} {r['category']}".lower()
        if words and not all(w in hay for w in words):
            continue
        if a.category and a.category.lower() not in r["category"].lower():
            continue
        if a.no_auth and r["auth"].lower() != "no":
            continue
        if a.https and r["https"].lower() != "yes":
            continue
        if a.cors and r["cors"].lower() != "yes":
            continue
        hits.append(r)

    print(f"{len(hits)} match(es)" + (f", showing {a.limit}" if len(hits) > a.limit else ""))
    for r in hits[: a.limit]:
        print(f"- {r['name']} [{r['category']}] auth={r['auth']} https={r['https']} cors={r['cors']}\n"
              f"  {r['description']}\n  {r['url']}")


if __name__ == "__main__":
    main()
