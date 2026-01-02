"""
Google Scholar MCP Server
========================

This module implements an MCP server for interacting with Google Scholar.
"""

from typing import Any, List, Dict, Optional
import asyncio
import logging
from mcp.server.fastmcp import FastMCP
from .search import search_google_scholar as _search_google_scholar

# Set up logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("google-scholar-mcp-server")

# Initialize FastMCP server for Google Scholar
mcp = FastMCP("google_scholar")


@mcp.tool()
async def search_google_scholar(
    query: str,
    author: Optional[str] = None,
    year_low: Optional[int] = None,
    year_high: Optional[int] = None,
    num_results: int = 5
) -> List[Dict[str, Any]]:
    """
    Search for articles on Google Scholar.
    Supports keyword search, author filtering, and year range filtering.
    
    Note: Providing the exact title and author name allows access to the complete abstract.

    Args:
        query: Search query string (paper title, topic, or keywords)
        author: Author name to filter results (optional)
        year_low: Start year for filtering (optional)
        year_high: End year for filtering (optional)
        num_results: Number of results to return (default: 5)

    Returns:
        List of dictionaries containing article information including:
        - bib: Bibliography info (title, author, year, venue, etc.)
        - abstract: Paper abstract
        - pub_url: Publication URL
        - num_citations: Number of citations
        - citedby_url: URL to citing papers
        - eprint_url: URL to eprint/PDF if available
    """
    logger.info(
        f"Searching Google Scholar: query={query}, author={author}, year_low={year_low}, year_high={year_high}, num_results={num_results}")
    try:
        results = await asyncio.to_thread(
            _search_google_scholar,
            query,
            author=author,
            year_low=year_low,
            year_high=year_high,
            num_results=num_results
        )
        return results
    except Exception as e:
        logger.error(f"Error searching Google Scholar: {str(e)}")
        return [{"error": f"An error occurred while searching Google Scholar: {str(e)}"}]
