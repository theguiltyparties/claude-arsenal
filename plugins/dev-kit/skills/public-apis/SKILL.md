---
name: public-apis
description: Find a free public API for a task by searching a catalog of ~2,400 APIs (from github.com/public-apis/public-apis) by keyword, category, whether it needs a key, HTTPS and CORS. Use when the user wants an API, data source or web service for something (weather, stocks, music, maps, sports, news, AI, government data...), asks "is there an API for...", or is building an app, bot, dashboard or automation that needs outside data.
---

# public-apis

Search the bundled catalog instead of guessing or reading the original 380 KB list.

## Search

```bash
python3 <skill-dir>/scripts/search_apis.py <keywords> [--no-auth] [--https] [--cors] [--category NAME] [--limit N]
python3 <skill-dir>/scripts/search_apis.py --list-categories
```

- Every keyword must appear in the name, description or category. Start broad
  (one or two words), then narrow. Try synonyms if nothing matches
  (e.g. `currency` / `exchange` / `forex`).
- `--no-auth`: no API key needed, so it works immediately. Prefer these for
  quick prototypes and demos.
- `--cors`: callable directly from browser JavaScript (web pages, artifacts).
  Without CORS the call has to go through a server or script.
- `--https`: required for anything served over HTTPS.

Output per API: name, category, auth (`No`, `apiKey`, `OAuth`, ...), HTTPS,
CORS, description and docs URL.

## How to use the results

1. Show the user the 3–5 best fits with why each fits, and say which need a
   key or sign-up.
2. Open the docs URL before writing code against an API. The catalog is a
   community list; endpoints, limits and pricing change, and some entries are
   dead. Check the API actually responds before relying on it.
3. Never invent keys. If an API needs one, tell the user where to get it and
   how you will read it (environment variable, not pasted into code).

## Refresh

The catalog is a snapshot. To pull the latest list (needs internet):

```bash
python3 <skill-dir>/scripts/search_apis.py --refresh
```
