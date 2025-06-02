# 🔁 Information Transformation and New Structure

## Criterion 3: Clear Transformation Requirements

- **Transformation Requirements**:
  - Convert unstructured HTML into clean, structured JSON
  - Use NLP to extract up to 100 individual terms or phrases from user text
  - Match these terms against known Investopedia URLs
  - Scrape and clean definitions from `<p id="mntl-sc-block_2-0">` or fallback to `div#short-definition__text_1-0`
- **New Feature Requirements**:
  - Input validation
  - Definition caching (planned)
  - Fallback handling for missing terms
  - Robust error management
  - Display logic for matched terms and links in the frontend

## Criterion 4: Substantial Change in Information Structure

- **Original Format**: HTML, no structure beyond visual layout
- **New Format**: Structured JSON, e.g.:

```json
{
  "term": "liquidity",
  "definition": "Liquidity refers to the efficiency...",
  "url": "https://www.investopedia.com/terms/l/liquidity.asp"
}
```

- **Substantial Changes**:
  - 🧠 New: Semantic structure (key-value pairing)
  - 📂 New: Format (HTML → JSON)
  - 🌐 New: Access method (UI + API instead of manual browsing)