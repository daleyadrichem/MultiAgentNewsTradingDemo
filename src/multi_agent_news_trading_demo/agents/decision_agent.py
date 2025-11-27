# ai_agents/decision_agent.py

from __future__ import annotations

from typing import Optional

from .utils import InvestmentRecommendation, SentimentResult, get_logger


class DecisionAgent:
    """Agent responsible for turning sentiment into a toy investment suggestion.

    IMPORTANT: This logic is intentionally simple and is designed purely
    for educational purposes in an AI demonstration. It must not be used
    for real-world investment decisions.
    """

    def __init__(
        self,
        bullish_threshold: float = 0.65,
        bearish_threshold: float = 0.65,
    ) -> None:
        """Initialize the decision agent.

        Parameters
        ----------
        bullish_threshold : float, optional
            Minimum score for a POSITIVE sentiment to be considered
            confidently bullish, by default 0.65.
        bearish_threshold : float, optional
            Minimum score for a NEGATIVE sentiment to be considered
            confidently bearish, by default 0.65.
        """
        self._logger = get_logger(self.__class__.__name__)
        self.bullish_threshold = bullish_threshold
        self.bearish_threshold = bearish_threshold

    def make_recommendation(
        self,
        sentiment: SentimentResult,
        recent_return: Optional[float] = None,
    ) -> InvestmentRecommendation:
        """Generate a toy investment suggestion based on sentiment.

        Parameters
        ----------
        sentiment : SentimentResult
            Sentiment of the article or summary text.
        recent_return : float, optional
            Recent percentage return of the asset (e.g. over the last
            few days), expressed as a decimal. For example, 0.02 means
            a 2% gain, -0.01 means a 1% loss, by default None.

        Returns
        -------
        InvestmentRecommendation
            Suggested action and explanation.

        Notes
        -----
        This is not financial advice. It is a didactic toy model used
        to demonstrate multi-agent AI workflows.
        """
        label = sentiment.label.upper()
        score = sentiment.score

        if label == "POSITIVE" and score >= self.bullish_threshold:
            base_rec = "CONSIDER INCREASING EXPOSURE (BUY BIAS)"
            base_conf = min(1.0, max(0.0, score))
            rationale = (
                "The sentiment on the article is strongly positive. "
                "In this toy model, we interpret this as a bullish signal."
            )
        elif label == "NEGATIVE" and score >= self.bearish_threshold:
            base_rec = "CONSIDER REDUCING EXPOSURE (SELL BIAS)"
            base_conf = min(1.0, max(0.0, score))
            rationale = (
                "The sentiment on the article is strongly negative. "
                "In this toy model, we interpret this as a bearish signal."
            )
        else:
            base_rec = "NO CLEAR SIGNAL (HOLD / NEUTRAL)"
            base_conf = 0.5
            rationale = (
                "The sentiment appears mixed or not confident enough "
                "to infer a clear directional signal."
            )

        # Optionally adjust confidence based on recent market direction
        if recent_return is not None:
            if recent_return > 0:
                rationale += (
                    f" Recent returns are positive (approx. {recent_return*100:.2f}%), "
                    "which slightly reinforces bullish signals."
                )
                if "BUY" in base_rec:
                    base_conf = min(1.0, base_conf + 0.05)
            elif recent_return < 0:
                rationale += (
                    f" Recent returns are negative (approx. {recent_return*100:.2f}%), "
                    "which slightly reinforces bearish signals."
                )
                if "SELL" in base_rec:
                    base_conf = min(1.0, base_conf + 0.05)

        self._logger.info(
            "Decision: %s (confidence=%.2f)", base_rec, base_conf
        )

        return InvestmentRecommendation(
            recommendation=base_rec,
            confidence=base_conf,
            rationale=rationale
            + " This is for educational purposes only and not real investment advice.",
        )
