# ai_agents/summary_agent.py

from __future__ import annotations

from typing import Optional

from .utils import NewsArticle, SummaryResult, clean_text, get_logger


class SummaryAgent:
    """Agent responsible for summarizing news articles.

    For a production system you might integrate an LLM or a dedicated
    summarization model. In this demo, we implement a simple extractive
    summarizer that selects the first N sentences.

    You can replace `_summarize_locally` with a call to your preferred
    LLM API (e.g. OpenAI) for a more powerful demo.
    """

    def __init__(self, max_sentences: int = 5) -> None:
        """Initialize the summary agent.

        Parameters
        ----------
        max_sentences : int, optional
            Maximum number of sentences to include in the summary,
            by default 5.
        """
        self._logger = get_logger(self.__class__.__name__)
        self.max_sentences = max_sentences

    def summarize_article(self, article: NewsArticle) -> SummaryResult:
        """Summarize a news article.

        Parameters
        ----------
        article : NewsArticle
            Article to summarize.

        Returns
        -------
        SummaryResult
            Summary text and meta-information about the summarization method.
        """
        self._logger.info(
            "Summarizing article: '%s' from source '%s'",
            article.title,
            article.source,
        )

        summary = self._summarize_locally(article.content)

        return SummaryResult(
            summary=summary,
            model_name="simple-first-n-sentences",
        )

    def _summarize_locally(self, text: str) -> str:
        """Very simple extractive summarization by taking the first N sentences.

        Parameters
        ----------
        text : str
            Article text.

        Returns
        -------
        str
            Extractive summary based on the first N sentences.
        """
        cleaned = clean_text(text)
        # Split on period; this is naive but okay for a teaching demo.
        sentences = [s.strip() for s in cleaned.split(".") if s.strip()]
        self._logger.info("Article contains %d sentences", len(sentences))

        selected = sentences[: self.max_sentences]
        return ". ".join(selected) + ("."
                                      if selected and not selected[-1].endswith(".")
                                      else "")
