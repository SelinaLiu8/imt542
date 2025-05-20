# IMT 542 Project: Stock Visualization Information Structure Access Guide

## About
This information structure supports a beginner-friendly stock visualization web application. It is designed for novice investors, students, and educators interested in understanding market trends through real-time and historical stock data. The structure allows users to query stock metrics like opening/closing prices, volume, and moving averages. Data is accessed via a Flask API and structured for educational and non-commercial use.

## Methodology
- Data is sourced from the Marketstack API using a registered access key.
- Only valid, high-volume tickers (e.g., AAPL, MSFT, GOOGL, AMZN, TSLA) are included.
- Data is fetched via scheduled jobs and stored in structured JSON format.
- The ETL pipeline includes validation steps to ensure completeness and consistency.
- Flask routes expose RESTful endpoints for querying ticker-specific data.
- Updates occur daily to ensure users receive near real-time market snapshots.
- Additional technical indicators (like SMA) are calculated during processing.
- All data is cached locally to avoid exceeding API rate limits.

## Access
1. Clone the repository and start the Flask server:
   ```bash
   git clone https://gitlab.com/your-org/stock-visualizer.git
   cd stock-visualizer
   python app.py
   ```
2. Open your browser and navigate to `http://localhost:5000` for the user interface.
3. Access the API directly for raw data:
   - `GET /api/stock/AAPL` – Returns the most recent data for Apple Inc.
   - `GET /api/stock/TSLA?start=2025-05-01&end=2025-05-16` – Returns historical data for Tesla in a date range.
4. Responses are in JSON format.
5. No authentication is required locally; production version will support API keys.

## Structure
Each stock record contains:
- `ticker` (string): Stock symbol (e.g., "MSFT")
- `date` (string, ISO 8601): Date of record
- `open` (float): Opening price
- `close` (float): Closing price
- `high` (float): Daily high
- `low` (float): Daily low
- `volume` (int): Volume of shares traded
- `sma_7` (float): 7-day simple moving average
- `sma_30` (float): 30-day simple moving average

## Example

### Example Request:
```http
GET /api/stock/GOOGL?start=2025-05-15&end=2025-05-16
```

### Example Response:
```json
[
  {
    "ticker": "GOOGL",
    "date": "2025-05-15",
    "open": 134.2,
    "close": 136.1,
    "high": 137.0,
    "low": 133.8,
    "volume": 15243000,
    "sma_7": 135.0,
    "sma_30": 132.1
  },
  {
    "ticker": "GOOGL",
    "date": "2025-05-16",
    "open": 136.2,
    "close": 138.0,
    "high": 138.5,
    "low": 135.9,
    "volume": 15890000,
    "sma_7": 136.1,
    "sma_30": 132.5
  }
]
```

> ⚠️ Note: The current system runs in demo mode. Data may differ slightly from live market values due to caching and API rate limits.
