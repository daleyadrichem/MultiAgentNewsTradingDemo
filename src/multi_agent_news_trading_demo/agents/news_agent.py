# ai_agents/news_agent.py

from __future__ import annotations

from datetime import datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup

from .utils import NewsArticle, clean_text, get_logger


class NewsAgent:
    """Agent responsible for retrieving news articles.

    This demo agent supports two modes:
    1. Fetch an article from a URL using basic HTML scraping.
    2. Accept a manually pasted article (title + content).

    Notes
    -----
    Real-world systems would use robust, legal, and reliable news APIs
    instead of ad-hoc scraping. This is simplified for teaching purposes.
    """

    def __init__(self) -> None:
        """Initialize the news agent."""
        self._logger = get_logger(self.__class__.__name__)

    def fetch_article_from_url(
        self,
        url: str,
        source_name: str = "Unknown Source",
    ) -> NewsArticle:
        """Fetch and parse a news article from a URL.

        Parameters
        ----------
        url : str
            URL of the news article.
        source_name : str, optional
            Human-readable name of the news source, by default "Unknown Source".

        Returns
        -------
        NewsArticle
            Parsed article containing title and main text.

        Raises
        ------
        RuntimeError
            If the article cannot be fetched or parsed.
        """
        self._logger.info("Fetching article from URL: %s", url)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            msg = f"Failed to fetch article from {url}: {exc}"
            self._logger.error(msg)
            raise RuntimeError(msg) from exc

        soup = BeautifulSoup(response.text, "html.parser")

        # Very naive extraction: try <title>, then <h1>, and all <p> tags.
        title_tag = soup.find("title") or soup.find("h1")
        title = clean_text(title_tag.get_text()) if title_tag else "Untitled article"

        paragraphs = [p.get_text() for p in soup.find_all("p")]
        content = clean_text(" ".join(paragraphs)) if paragraphs else ""

        if not content:
            msg = f"Could not extract article content from {url}"
            self._logger.error(msg)
            raise RuntimeError(msg)

        self._logger.info("Successfully parsed article: %s", title)

        return NewsArticle(
            title=title,
            content=content,
            source=source_name,
            url=url,
            published_at=None,  # Could be parsed from meta tags in a more advanced version
        )

    def create_article_from_manual_input(
        self,
        title: str,
        content: str,
        source_name: str = "Manual Input",
        published_at: Optional[datetime] = None,
    ) -> NewsArticle:
        """Create a news article instance from manually provided text.

        This is useful when scraping is not possible or not desired.
        You can simply copy-paste a news article into the notebook and
        construct a :class:`NewsArticle` from it.

        Parameters
        ----------
        title : str
            Title of the article.
        content : str
            Full text of the article.
        source_name : str, optional
            Name of the news source, by default "Manual Input".
        published_at : datetime, optional
            Publication timestamp, by default None.

        Returns
        -------
        NewsArticle
            Structured article instance.
        """
        self._logger.info(
            "Creating article from manual input, title='%s', source='%s'",
            title,
            source_name,
        )
        return NewsArticle(
            title=clean_text(title),
            content=clean_text(content),
            source=source_name,
            url=None,
            published_at=published_at,
        )
