import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

def load_data() -> pd.DataFrame:
    """Load data from PostgreSQL."""
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM stock_prices", engine)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def plot_closing_prices(df: pd.DataFrame) -> None:
    """Chart 1 — Closing prices over time for all stocks."""
    plt.figure(figsize=(12, 6))
    for ticker in df["ticker"].unique():
        stock_df = df[df["ticker"] == ticker]
        plt.plot(stock_df["Date"], stock_df["Close"], label=ticker)
    
    plt.title("Stock Closing Prices (6 Months)", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("closing_prices.png")
    print("✅ Saved closing_prices.png")
    plt.show()

def plot_daily_returns(df: pd.DataFrame) -> None:
    """Chart 2 — Daily returns distribution per stock."""
    plt.figure(figsize=(12, 6))
    for ticker in df["ticker"].unique():
        stock_df = df[df["ticker"] == ticker]
        sns.kdeplot(stock_df["daily_return"], label=ticker)

    plt.title("Daily Returns Distribution", fontsize=16)
    plt.xlabel("Daily Return")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig("daily_returns.png")
    print("✅ Saved daily_returns.png")
    plt.show()

def plot_moving_average(df: pd.DataFrame) -> None:
    """Chart 3 — 7-day moving average per stock."""
    plt.figure(figsize=(12, 6))
    for ticker in df["ticker"].unique():
        stock_df = df[df["ticker"] == ticker]
        plt.plot(stock_df["Date"], stock_df["ma_7"], label=ticker)

    plt.title("7-Day Moving Average", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("moving_average.png")
    print("✅ Saved moving_average.png")
    plt.show()

# Run all charts
if __name__ == "__main__":
    print("📊 Generating dashboard...")
    df = load_data()
    plot_closing_prices(df)
    plot_daily_returns(df)
    plot_moving_average(df)
    print("✅ Dashboard complete!")