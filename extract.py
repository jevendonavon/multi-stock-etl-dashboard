import yfinance as yf
import pandas as pd

def extract_multiple_stocks(tickers: list, period: str = "6mo") -> pd.DataFrame:
    """
    Extract stock data for multiple tickers at once.
    tickers: list of stock symbols e.g. ["AAPL", "MSFT", "GOOGL"]
    period: how far back to pull data
    """
    all_data = []  # empty list to collect each stock's data

    for ticker in tickers:
        print(f"Extracting {ticker}...")
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        df = df.reset_index()
        df["ticker"] = ticker
        all_data.append(df)  # add to our list

    # Combine all stocks into one big table
    combined_df = pd.concat(all_data, ignore_index=True)

    print(f"✅ Extracted {len(combined_df)} total rows for {len(tickers)} stocks")
    return combined_df

# Test it
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    df = extract_multiple_stocks(tickers)
    print(df.head(10))
    print(f"\nStocks extracted: {df['ticker'].unique()}")

