# ai_agents/__init__.py

"""Multi-agent AI demo package for investment-related workflows.

This package is intended for teaching and workshop purposes.
It must not be used for real-world investment decisions.
"""

from .stock_agent import StockDataAgent
from .news_agent import NewsAgent
from .summary_agent import SummaryAgent
from .sentiment_agent import SentimentAgent
from .decision_agent import DecisionAgent
from .utils import (
    NewsArticle,
    SummaryResult,
    SentimentResult,
    InvestmentRecommendation,
)

__all__ = [
    "StockDataAgent",
    "NewsAgent",
    "SummaryAgent",
    "SentimentAgent",
    "DecisionAgent",
    "NewsArticle",
    "SummaryResult",
    "SentimentResult",
    "InvestmentRecommendation",
]
