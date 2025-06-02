# ⚙️ Functional Access to New Portable Information

## Criterion 5: Functional System Access

- **System Components**:
  - React Frontend (hosted on GitHub Pages)
  - Flask Backend (hosted on Azure Web App)
- **Endpoints**:
  - `PUT /input`: Accepts user paragraph and stores terms for processing
  - `GET /definitions`: Returns matched terms with definitions and URLs
- **Frontend Features**:
  - Textarea input for up to 100 words
  - Displays structured results with clickable URLs
- **Access Method**:
  - Public URL (no login required)
  - CORS enabled to allow cross-origin access from frontend to backend

## Criterion 6: Accuracy and Completeness

- **Correctness**:
  - Definitions matched exactly by string comparison (single words, bigrams, trigrams)
  - Fallback logic ensures a match is attempted for multiple HTML structures
- **Completeness**:
  - Only valid Investopedia terms are returned
  - Unknown terms return `null` to preserve output integrity
  - API responses are structured and ready for display or reuse