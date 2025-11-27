# ai_agents/stock_agent.py

from __future__ import annotations

from typing import Optional

import pandas as pd
import yfinance as yf

from .utils import get_logger


class StockDataAgent:
    """Agent responsible for retrieving stock market data.

    This implementation uses `yfinance` to query Yahoo Finance, which is
    convenient for demos because it does not require an API key.

    Examples
    --------
    >>> agent = StockDataAgent()
    >>> df = agent.get_index_history(symbol="^GSPC", period="1y", interval="1d")
    >>> df.tail()
    """

    def __init__(self) -> None:
        """Initialize the stock data agent."""
        self._logger = get_logger(self.__class__.__name__)

    def get_index_history(
        self,
        symbol: str = "^GSPC",
        period: str = "1y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        """Fetch historical prices for an index or stock.

        Parameters
        ----------
        symbol : str, optional
            Ticker symbol, by default "^GSPC" (S&P 500 index).
        period : str, optional
            History period, e.g. "1y", "6mo", "5d", by default "1y".
        interval : str, optional
            Data frequency, e.g. "1d", "1h", by default "1d".

        Returns
        -------
        pandas.DataFrame
            DataFrame with OHLCV price data indexed by date.

        Raises
        ------
        ValueError
            If no data is returned for the given parameters.
        """
        self._logger.info(
            "Fetching price history for symbol=%s, period=%s, interval=%s",
            symbol,
            period,
            interval,
        )
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)

        if df.empty:
            msg = f"No data returned for symbol={symbol}, period={period}, interval={interval}"
            self._logger.error(msg)
            raise ValueError(msg)

        self._logger.info("Retrieved %d rows of price data", len(df))
        return df

    @staticmethod
    def compute_recent_return(
        price_history: pd.DataFrame, lookback_days: int = 5
    ) -> Optional[float]:
        """Compute a simple percentage return over a recent lookback window.

        Parameters
        ----------
        price_history : pandas.DataFrame
            Historical price data as returned by :meth:`get_index_history`.
        lookback_days : int, optional
            Number of trading rows to look back, by default 5.

        Returns
        -------
        float or None
            Percentage return over the lookback window. If there are not
            enough rows in `price_history`, ``None`` is returned.
        """
        if len(price_history) < lookback_days + 1:
            return None

        # Use the 'Close' price for a simple return calculation
        recent = price_history["Close"].iloc[-(lookback_days + 1) :]
        start_price = recent.iloc[0]
        end_price = recent.iloc[-1]
        return float((end_price - start_price) / start_price)
