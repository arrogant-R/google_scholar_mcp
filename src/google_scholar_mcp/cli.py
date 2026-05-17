#!/usr/bin/env python3
"""Command-line interface for Google Scholar search."""

import sys
import json
import argparse

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from .search import search_google_scholar, get_publication_bibtex


def main():
    parser = argparse.ArgumentParser(
        prog="google-scholar",
        description="Search Google Scholar from the command line",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # search subcommand
    search_parser = subparsers.add_parser("search", help="Search for articles")
    search_parser.add_argument("query", help="Search query string")
    search_parser.add_argument("--author", default=None, help="Filter by author name")
    search_parser.add_argument("--year-low", type=int, default=None, help="Start year (inclusive)")
    search_parser.add_argument("--year-high", type=int, default=None, help="End year (inclusive)")
    search_parser.add_argument(
        "--num-results", type=int, default=5, help="Number of results (default: 5)"
    )
    search_parser.add_argument(
        "--no-fill", action="store_true", help="Skip filling detailed info (faster)"
    )

    # bibtex subcommand
    bibtex_parser = subparsers.add_parser("bibtex", help="Get BibTeX citation")
    bibtex_parser.add_argument("query", help="Search query (paper title)")
    bibtex_parser.add_argument(
        "--num-results", type=int, default=1, help="Number of entries (default: 1)"
    )

    args = parser.parse_args()

    if args.command == "search":
        results = search_google_scholar(
            query=args.query,
            author=args.author,
            year_low=args.year_low,
            year_high=args.year_high,
            num_results=args.num_results,
            fill_details=not args.no_fill,
        )
        print(json.dumps(results, ensure_ascii=False, indent=2))

    elif args.command == "bibtex":
        entries = get_publication_bibtex(query=args.query, num_results=args.num_results)
        for entry in entries:
            print(entry)
            print()

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
