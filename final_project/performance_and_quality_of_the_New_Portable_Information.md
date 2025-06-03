# 🧪 **Performance and Quality of the New Portable Information**

## Criterion 1: Term Accuracy & Definition Clarity

- **Extraction Logic**:
  - Financial terms are extracted using NLP techniques (tokenization + n-grams)
  - Terms are matched against known Investopedia pages
  - Scraper checks for both short and long definitions in structured HTML blocks

- **Output Format**:
  - Clean, flat JSON structure with `term`, `definition`, and `url` fields
  - Standardized layout ensures readability and easy integration

- **Validation**:
  - Only valid, matched terms return results
  - Errors are logged and handled gracefully (e.g., no crash on missing tag)

---

## Criterion 2: Performance and System Responsiveness

- **Initial Query Time**:
  - Most single-term queries return within **1–2 seconds**

- **API Performance**:
  - PUT `/input`: Stores the user’s raw paragraph (≤100 words)
  - GET `/definitions`: Extracts, scrapes, and returns matches as JSON
  - Endpoint responses tested across varying inputs and network conditions

- **Scalability**:
  - Lightweight design allows for integration into education apps, dashboards, or chatbots
  - Performance logs show consistent latency with minimal variance

---

## Criterion 3: Resilience and Stability

- **Scraping Strategy**:
  - Uses tag-based scraping with stable `id` and `class` selectors
  - Resilient to minor HTML structure changes

- **Error Handling**:
  - Gracefully skips unmatched terms
  - Logs missing or malformed elements for review

- **Output Reliability**:
  - Clean JSON always returned, even when partial matches occur

