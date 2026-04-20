import pandas as pd

def transform_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich stock data for multiple tickers.
    """
    print("Transforming data...")

    # 1. Keep only columns we need
    df = df[["Date", "Open", "High", "Low", "Close", "Volume", "ticker"]].copy()

    # 2. Remove timezone from Date
    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    # 3. Round prices to 2 decimal places
    for col in ["Open", "High", "Low", "Close"]:
        df[col] = df[col].round(2)
        
    # 4. Calculate daily return per stock
    df["daily_return"] = (
        df.groupby("ticker")["Close"]
        .pct_change()
        .round(4)
    )

    # 5. Calculate 7-day moving average per stock
    df["ma_7"] = (
        df.groupby("ticker")["Close"]
        .transform(lambda x: x.rolling(window=7).mean())
        .round(2)
    )

    # 6. Drop rows with nulls
    df = df.dropna()

    print(f"✅ Transformed {len(df)} rows for {df['ticker'].nunique()} stocks")
    return df

# Test it
if __name__ == "__main__":
    from extract import extract_multiple_stocks
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    df = extract_multiple_stocks(tickers)
    df_transformed = transform_stock_data(df)
    print(df_transformed.head(10))
    print(f"\nUnique stocks: {df_transformed['ticker'].unique()}")