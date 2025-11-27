# ai_agents/sentiment_agent.py

from __future__ import annotations

from typing import Optional

from transformers import pipeline

from .utils import SentimentResult, clean_text, get_logger


class SentimentAgent:
    """Agent responsible for sentiment analysis of text.

    This demo uses a Transformers sentiment-analysis pipeline.
    It maps the model's output to POSITIVE, NEGATIVE, or NEUTRAL.
    """

    def __init__(
        self,
        model_name: str = "distilbert-base-uncased-finetuned-sst-2-english",
        neutral_margin: float = 0.1,
    ) -> None:
        """Initialize the sentiment agent.

        Parameters
        ----------
        model_name : str, optional
            HuggingFace model name, by default
            "distilbert-base-uncased-finetuned-sst-2-english".
        neutral_margin : float, optional
            Margin around 0.5 probability to consider as NEUTRAL,
            by default 0.1.
        """
        self._logger = get_logger(self.__class__.__name__)
        self.model_name = model_name
        self.neutral_margin = neutral_margin
        self._logger.info("Loading sentiment model: %s", model_name)
        self._pipeline = pipeline("sentiment-analysis", model=model_name)

    def analyze_text(self, text: str) -> SentimentResult:
        """Run sentiment analysis on the given text.

        Parameters
        ----------
        text : str
            Input text (full article or summary).

        Returns
        -------
        SentimentResult
            Structured sentiment analysis result.
        """
        cleaned = clean_text(text)
        if not cleaned:
            self._logger.warning("Empty text provided to SentimentAgent")
            return SentimentResult(
                label="NEUTRAL",
                score=0.0,
                model_name=self.model_name,
            )

        self._logger.info("Running sentiment analysis on text of length %d", len(cleaned))
        output = self._pipeline(cleaned[: 512])[0]  # truncate for speed

        raw_label: str = str(output["label"]).upper()
        score: float = float(output["score"])

        # Map binary label + score into POSITIVE/NEGATIVE/NEUTRAL
        if abs(score - 0.5) <= self.neutral_margin:
            label = "NEUTRAL"
        else:
            if "NEG" in raw_label:
                label = "NEGATIVE"
            else:
                label = "POSITIVE"

        self._logger.info("Sentiment result: label=%s, score=%.3f", label, score)

        return SentimentResult(label=label, score=score, model_name=self.model_name)
