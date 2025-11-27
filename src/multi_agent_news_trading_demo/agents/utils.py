# ai_agents/utils.py

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


def get_logger(name: str) -> logging.Logger:
    """Create and configure a logger.

    Parameters
    ----------
    name : str
        Name of the logger, typically `__name__` of the calling module.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def clean_text(text: str) -> str:
    """Minimal text normalization.

    This is intentionally simple for demo purposes.

    Parameters
    ----------
    text : str
        Raw input text.

    Returns
    -------
    str
        Cleaned text.
    """
    return " ".join(text.strip().split())


@dataclass
class NewsArticle:
    """Container for a news article."""

    title: str
    content: str
    source: str
    url: Optional[str] = None
    published_at: Optional[datetime] = None


@dataclass
class SummaryResult:
    """Container for a summarization result."""

    summary: str
    model_name: str


@dataclass
class SentimentResult:
    """Container for a sentiment analysis result."""

    label: str
    score: float
    model_name: str


@dataclass
class InvestmentRecommendation:
    """Container for an investment suggestion.

    Notes
    -----
    This is intended strictly for educational and demonstration purposes.
    It must not be used as real financial advice.
    """

    recommendation: str
    confidence: float
    rationale: str
