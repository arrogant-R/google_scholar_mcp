"""
Google Scholar MCP Server initialization
"""

from .server import mcp
from .search import search_google_scholar
import asyncio


def main():
    """Main entry point for the package."""
    mcp.run()


__all__ = ["main", "mcp"]
