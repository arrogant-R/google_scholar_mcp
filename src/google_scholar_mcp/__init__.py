"""
Google Scholar MCP Server initialization
"""

from .server import mcp
import asyncio


def main():
    """Main entry point for the package."""
    mcp.run()


__all__ = ["main", "mcp"]
