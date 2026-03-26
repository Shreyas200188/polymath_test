# AI Commerce Discovery – Improving Visibility for Shopify Merchants

## Overview

This project explores why high-quality Shopify merchants fail to appear in AI-powered shopping results, and proposes a practical backend solution to improve their discoverability.

Instead of building a UI, this project focuses on how modern AI agents (e.g., ChatGPT, Claude, Perplexity) discover, interpret, and retrieve product information from websites — and how we can optimize for that pipeline.

---

## Problem

A Shopify merchant with:

* Strong SEO
* High-quality products
* Good reviews

…still does not appear in AI-driven shopping experiences.

Why?

Because AI agents do **not rely on traditional SEO alone**. They depend on:

* Structured data
* Crawlable and clean content
* Semantic understanding
* External signals and embeddings

---

## Goal

Build a system that:

1. Simulates how AI agents currently discover products (**baseline**)
2. Improves product representation using structured + semantic techniques (**enhanced pipeline**)
3. Demonstrates improved retrieval quality

---

## Approach

### 1. Baseline Pipeline (Current AI Discovery)

* Input: Raw product page (HTML)
* Steps:

  * Scrape visible content
  * Extract text
  * Use naive keyword matching
* Output:

  * Poorly structured product representation

---

### 2. Enhanced Pipeline (Proposed Solution)

We improve discoverability by transforming the product data into formats that AI systems prefer.

#### Key Enhancements:

* Structured extraction (title, price, reviews, specs)
* Schema enrichment (JSON-LD style data)
* AI-generated product summaries
* Embedding generation for semantic retrieval
* Query → product matching using vector similarity

---

## System Architecture

```
Raw Product Page
        ↓
   Scraper
        ↓
   Parser
        ↓
 -------------------------
| Baseline Representation |
 -------------------------
        ↓

 -------------------------
| Enhanced Representation |
| - Structured JSON       |
| - AI Summary            |
| - Embeddings            |
 -------------------------
        ↓
   Retrieval Engine
        ↓
   Ranked Results
```

---

## Project Structure

```
polymath_test/
│
├── src/
│   ├── main.py
│   ├── scraper.py
│   ├── parser.py
│   ├── enhancer.py
│   ├── embeddings.py
│   ├── retriever.py
│
├── data/
│   └── sample_products.json
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/Shreyas200188/polymath_test.git
cd polymath_test

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python src/main.py
```

---

## Example Flow

1. Load sample Shopify product pages
2. Run baseline extraction
3. Run enhanced pipeline
4. Compare retrieval results for sample queries

---

## Key Insight

AI agents prefer:

* Clean structured data over raw HTML
* Semantic meaning over keywords
* Context-rich summaries over fragmented text

This project demonstrates how small backend changes can significantly improve visibility in AI-driven commerce.

---

## Future Improvements

* Real Shopify API integration
* Multi-product ranking benchmarks
* External signal integration (reviews, Reddit, etc.)
* Fine-tuned ranking models

---

## Why This Matters

As AI becomes the primary interface for discovery, traditional SEO is no longer enough.

Merchants must optimize for:

> “AI readability” instead of just “search engine ranking”

This project is a step in that direction.

## 🟢 Progress Update (Phase-wise Summary)

### Initial Baseline
- Loaded products from `products.json`.
- Implemented **simple keyword-based retrieval**.
- Displayed basic query results using product titles and prices.

### Phase 1 — Structured Extraction
- Created `structured_extractor.py`.
- Extracted structured data from product titles and descriptions:
  - `category`
  - `use_case`
  - `features` (adjectives/keywords)
- Initially used simple heuristics (hard-coded for shoes), now replaced with **fully generic noun/adjective extraction** using spaCy.

### Phase 2 — Query Understanding
- Created `query_understanding.py`.
- Implemented **query normalization and expansion**:
  - Mapped synonyms and intents (e.g., "marathon" → "running", "office" → "formal").
  - Expanded query terms to improve structured retrieval.

### Phase 3 — Enhancement
- Created `enhancer.py`.
- Added **automatic summaries** for structured products.
- Normalized product data for more readable outputs.

### Phase 4 — Semantic Retrieval
- Created `semantic_retriever.py` using **TF-IDF**:
  - Converts product descriptions to vector representations.
  - Computes similarity with normalized queries for better ranking.

### Current Improvements Over Baseline
- Generic, **domain-agnostic structured extraction** (works for any product type, not just shoes).
- Query understanding layer for better intent mapping.
- Structured and semantic retrieval **rank products more accurately**.
- Added product summaries and feature extraction for **explainable results**.
- Semantic similarity ensures relevant products appear even if keywords don’t match exactly.

**Next Planned Phases**
- Upgrade semantic retrieval to **vector embeddings** (OpenAI or Sentence-Transformers).
- Integrate **cosine similarity search** for improved ranking.
- Add a **mini LLM-based feature/summary generator** for richer structured data.