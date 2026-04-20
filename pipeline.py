from extract import extract_multiple_stocks
from transform import transform_stock_data
from load import load_stock_data

def run_pipeline(tickers: list, period: str = "6mo") -> None:
    """
    Run the full ETL pipeline for multiple stocks.
    """
    print("🚀 Starting ETL Pipeline...")
    print(f"Stocks: {tickers}")
    print("-" * 40)

    # Step 1 - Extract
    df = extract_multiple_stocks(tickers, period)

    # Step 2 - Transform
    df = transform_stock_data(df)

    # Step 3 - Load
    load_stock_data(df)

    print("-" * 40)
    print("✅ Pipeline completed successfully!")

# Run it
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    run_pipeline(tickers)