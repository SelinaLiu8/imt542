# 📘 Investopedia Definition Extractor

## 🧩 About

This system is a web-based tool designed to extract financial term definitions from Investopedia given any user-provided paragraph (up to 100 words). It targets students, analysts, or non-experts who need to quickly understand terminology embedded in financial writing. The audience includes those in business intelligence, finance education, or financial technology. The application is accessed via a simple React frontend that connects to a Flask-based API running locally or remotely.

---

## 🔬 Methodology

- The input paragraph is parsed and cleaned using Python NLP techniques.
- It tokenizes the paragraph into single words, bigrams, and trigrams to detect potential financial terms.
- Each term candidate is checked for a valid Investopedia definition using URL-based scraping.
- The system first attempts to retrieve definitions via `https://www.investopedia.com/terms/{first-letter}/{slug}.asp`.
- If the direct path fails, it falls back to searching the term on DuckDuckGo restricted to Investopedia.
- Definitions are parsed using BeautifulSoup from tags like `<p id="mntl-sc-block_2-0">` and `<div id="short-definition__text_1-0">`.
- Only terms that return a valid definition and URL are included in the output.
- The API supports a PUT request to update the input and a GET request to retrieve definitions.
- Cross-origin requests from the frontend are handled using `flask-cors`.

---

## 🔑 Access

- **Frontend**: Start the React application (e.g., `npm start`) which runs at `http://localhost:3000`.
- **Backend**: Start the Flask API (e.g., `python app.py`) which runs at `http://localhost:5050`.
- **Input**:
  - Use the frontend interface to paste or type your paragraph.
  - On submission, the React app sends a `PUT` request to `/input`.
- **Processing**:
  - Flask saves the paragraph to `input.txt`, extracts terms, and scrapes Investopedia definitions.
- **Output**:
  - React calls `GET /definitions` to fetch a JSON array of matching terms with definitions and URLs.
- Ensure both servers are running simultaneously and that `flask-cors` is enabled for communication.

---

## 🗃️ Structure

Each definition is returned as an object in a JSON array with the following schema:

| Field       | Type   | Description                                                |
|-------------|--------|------------------------------------------------------------|
| `term`      | string | The financial term or phrase detected in the paragraph     |
| `definition`| string | A brief definition pulled from Investopedia                |
| `url`       | string | Direct link to the Investopedia article for further reading|

---

## 📥 Example

### Example Request (Frontend React):
```json
PUT /input
{
  "text": "In a bear market, return on equity and dividend yield are key metrics for financial analysis."
}

GET/output
[
  {
    "term": "bear market",
    "definition": "A bear market is a market condition where investors are more risk-averse...",
    "url": "https://www.investopedia.com/terms/b/bearmarket.asp"
  },
  {
    "term": "return on equity",
    "definition": "Return on equity (ROE) is a measure of financial performance...",
    "url": "https://www.investopedia.com/terms/r/returnonequity.asp"
  },
  {
    "term": "dividend yield",
    "definition": "The dividend yield is a financial ratio that shows how much a company pays out...",
    "url": "https://www.investopedia.com/terms/d/dividendyield.asp"
  }
]