import numpy as np
import pandas as pd
import yfinance as yf
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent


def resolve_path(file_path: str, create_dirs: bool = False) -> Path:
    """
    Helper for resolving relative paths
    """
    path = Path(file_path) if Path(file_path).is_absolute() else PROJECT_ROOT / file_path
    if create_dirs:
        path.parent.mkdir(parents=True, exist_ok=True)
    return path


def download_data(ticker: str, start: str, end: str, save: bool = False) -> pd.DataFrame:
    """
    Download data from yahoo finance and return them, optionally save them to csv

    :param ticker: Asset ticker (e.g. 'AAPL')
    :type ticker: str
    :param start: Start date in 'YYYY-MM-DD' format
    :type start: str
    :param end: End date in 'YYYY-MM-DD' format
    :type end: str
    :param save: Optionally save data to csv (default False)
    :type save: bool (optional)

    :return: Daily adjusted close prices indexed by date
    :rtype: pd.DataFrame
    """
    df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
    assert len(df) > 0, "YF error"

    df = df.sort_values("Date").reset_index()
    df.columns = df.columns.droplevel("Ticker")
    df.columns.name = None
    df["Ticker"] = ticker
    path = resolve_path(f"data/{ticker}.csv", create_dirs=True)
    cols = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    df = df[cols]
    if save:
        df.to_csv(path, index=False)

    return df


def load_data(data_path: str) -> pd.DataFrame:
    """
    Load data from csv
    """
    path = resolve_path(data_path)
    df = pd.read_csv(path)
    df = df.sort_values("Date").reset_index(drop=True)

    return df
