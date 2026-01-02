"""Search functionality for the Google Scholar MCP server."""

from .scholarly import scholarly
from typing import Optional, List, Dict, Any


def search_google_scholar(
    query: str,
    author: Optional[str] = None,
    year_low: Optional[int] = None,
    year_high: Optional[int] = None,
    num_results: int = 5,
    fill_details: bool = True
) -> List[Dict[str, Any]]:
    """
    Unified function to search Google Scholar using scholarly library.
    Supports keyword search, author filtering, and year range filtering.

    Parameters:
    -----------
    query : str
        The search query (e.g., paper title, topic, or keywords).
    author : str, optional
        The author's name to filter the results (default is None).
    year_low : int, optional
        The start year to filter results (default is None).
    year_high : int, optional
        The end year to filter results (default is None).
    num_results : int
        The number of results to retrieve (default is 5).
    fill_details : bool
        Whether to fill in complete publication details (default is True).
        Setting to False is faster but returns less information.

    Returns:
    --------
    list
        A list of dictionaries containing search results with bib info.
    """
    results = []

    # Build query with author if specified
    search_query_str = query
    if author:
        search_query_str = f"{query} author:{author}"

    # Use scholarly's search with year range if specified
    if year_low is not None or year_high is not None:
        search_query = scholarly.search_pubs(
            search_query_str,
            year_low=year_low,
            year_high=year_high
        )
    else:
        search_query = scholarly.search_pubs(search_query_str)

    count = 0
    for pub in search_query:
        if count >= num_results:
            break

        # Optionally fill in complete publication details
        if fill_details:
            pub = scholarly.fill(pub)

        # Extract bib information
        bib = pub.get('bib', {})

        result_data = {
            'bib': bib,
            'abstract': bib.get('abstract', 'No abstract available'),
            'pub_url': pub.get('pub_url', ''),
            'num_citations': pub.get('num_citations', 0),
            'citedby_url': pub.get('citedby_url', ''),
            'eprint_url': pub.get('eprint_url', '')
        }
        results.append(result_data)
        count += 1

    return results


def get_publication_bibtex(query: str, num_results: int = 1) -> List[str]:
    """
    Get BibTeX entries for publications matching the query.

    Parameters:
    -----------
    query : str
        The search query (e.g., paper title).
    num_results : int
        The number of BibTeX entries to retrieve.

    Returns:
    --------
    list
        A list of BibTeX strings.
    """
    bibtex_entries = []
    search_query = scholarly.search_pubs(query)

    count = 0
    for pub in search_query:
        if count >= num_results:
            break

        pub_filled = scholarly.fill(pub)
        bibtex = scholarly.bibtex(pub_filled)
        bibtex_entries.append(bibtex)
        count += 1

    return bibtex_entries
