---
name: google-scholar-search
description: >
  Search Google Scholar for academic papers. Provides keyword search with author
  filtering, year range filtering, full abstract retrieval, BibTeX citation
  export, and CAPTCHA handling. Use when the user asks to search academic
  papers, find scholarly articles, look up citations, get BibTeX references,
  or any query involving Google Scholar, academic research, or scientific
  literature. Triggers include "search scholar", "find papers", "academic
  search", "论文搜索", "学术搜索", "Google Scholar", "文献检索", "BibTeX",
  "引用格式".
---

# Google Scholar Search

Search Google Scholar academic papers via the `scholarly` library (modified version with CAPTCHA handling).

## Quick Start

```bash
# Basic keyword search (returns JSON)
google-scholar search "attention is all you need" --num-results 3

# Search with author filter
google-scholar search "deep learning" --author "Yann LeCun"

# Search with year range
google-scholar search "transformer" --year-low 2020 --year-high 2024 --num-results 5

# Get BibTeX citation
google-scholar bibtex "attention is all you need"
```

## Prerequisites

Install the `google-scholar-mcp` package (provides the `google-scholar` CLI):

```bash
# Via uv (recommended — fast, no proxy issues)
uv tool install google_scholar_mcp

# Or install from GitHub
uv tool install git+https://github.com/arrogant-R/google_scholar_mcp.git
```

> ⚠️ **Avoid `pip install`** — pip is slow and may fail behind proxies. Use `uv` instead.

## Commands

### search

```bash
google-scholar search "<query>" [options]
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `query` | str | required | Search keywords (title, topic, or terms) |
| `--author` | str | None | Filter by author name |
| `--year-low` | int | None | Start year (inclusive) |
| `--year-high` | int | None | End year (inclusive) |
| `--num-results` | int | 5 | Number of results to return |
| `--no-fill` | flag | off | Skip detailed info (faster, less data) |

**Output**: JSON array. Each item contains:

```json
{
  "bib": { "title": "...", "author": "...", "pub_year": "...", "venue": "...", "abstract": "..." },
  "abstract": "Full abstract text",
  "pub_url": "https://...",
  "num_citations": 12345,
  "citedby_url": "https://...",
  "eprint_url": "https://..."
}
```

### bibtex

```bash
google-scholar bibtex "<query>" [--num-results N]
```

**Output**: BibTeX entry strings printed to stdout.

## CAPTCHA Handling

When Google Scholar detects automated access, a CAPTCHA popup appears. The modified `scholarly` library:

1. Auto-detects the CAPTCHA challenge
2. Opens a browser window for manual verification
3. Syncs cookies after verification for subsequent requests
4. Persists cookies locally to reduce future CAPTCHA triggers

If a CAPTCHA is encountered, inform the user: "Google Scholar requires CAPTCHA verification. A browser window should have appeared — please complete the verification manually, then I'll retry the search."

## Tips

- Use precise queries (full title + author) to get complete abstracts
- Use `--no-fill` for quick result counts without detailed metadata
- For citation chains, use the `citedby_url` from search results
- Year ranges are inclusive on both ends
