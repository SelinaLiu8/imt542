# 📘 Information Story

## 🎯 Problem

Understanding financial concepts can be overwhelming—especially when information is buried in long, article-style formats not optimized for quick lookup or automation. Platforms like Investopedia offer high-quality definitions, but they are designed for human reading, not machine processing. There’s currently no simple way for users to input a financial paragraph and receive contextual definitions automatically.

---

## 👤 Target Audience

- 📚 **Students and new investors** seeking to improve financial literacy
- 🧑‍🏫 **Educators** building materials for finance-related courses
- 🧠 **Self-learners** looking for in-context understanding
- 🛠️ **Developers and product teams** who want to embed finance term definitions in their apps or tools

---

## 💡 What Our Tool Does

- Accepts a paragraph of up to 100 words (free-form text input)
- Automatically identifies financial terms using NLP (tokenization + bigram/trigram matching)
- Extracts definitions from Investopedia using tag-based HTML scraping
- Returns the results as structured, portable JSON (term, definition, and source URL)
- Exposes this information via a simple REST API

---

## 📦 Scope

**In Scope**
- Text input up to 100 words
- Term detection and matching with Investopedia URLs
- REST API access via PUT `/input` and GET `/definitions`
- JSON-formatted output (term, definition, URL)

**Out of Scope**
- Non-English content
- CSV or PDF inputs
- Predictive modeling or financial advice
- Definitions not present in Investopedia

---

## 🧭 Why This Matters

This project makes financial definitions **portable** by transforming unstructured content into clean, reusable data. With just one API call, users can integrate contextual definitions into websites, learning tools, or chatbots. By re-structuring this knowledge into JSON and exposing it via API, we turn static web content into a dynamic educational resource that promotes **faster learning**, **automation**, and **knowledge accessibility**.

---

