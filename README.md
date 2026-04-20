# multi-stock-etl-dashboard
ETL pipeline for multiple # Multi-Stock ETL Dashboard 📊

ETL pipeline that extracts data for multiple stocks, 
transforms it, and visualizes it with charts.

## What it does
- **Extract** — Fetches data for multiple stocks at once (AAPL, MSFT, GOOGL, AMZN)
- **Transform** — Cleans data, calculates daily return & 7-day moving average
- **Load** — Stores all stocks into PostgreSQL
- **Dashboard** — Generates 3 charts: closing prices, daily returns, moving average

## Tech Stack
- Python
- Pandas
- yFinance
- SQLAlchemy
- PostgreSQL
- Matplotlib
- Seaborn

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your `.env` file with DB credentials
4. Run pipeline: `python pipeline.py`
5. Generate charts: `python dashboard.py`stocks with data visualization dashboard
