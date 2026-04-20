import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    """Create a connection to PostgreSQL."""
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    return engine

def load_stock_data(df: pd.DataFrame, table_name: str = "stock_prices") -> None:
    """Load transformed data into PostgreSQL."""
    print(f"Loading data into '{table_name}'...")
    engine = get_engine()
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"✅ Loaded {len(df)} rows into '{table_name}' table")

# Test it
if __name__ == "__main__":
    from extract import extract_multiple_stocks
    from transform import transform_stock_data

    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    df = extract_multiple_stocks(tickers)
    df = transform_stock_data(df)
    load_stock_data(df)