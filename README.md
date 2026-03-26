# AI Commerce Discovery – Making Shopify Merchants Visible to AI Shopping Agents

## The Problem This Solves

A Shopify merchant has been running their store for 5 years. They have great products, strong reviews, and solid SEO. But when a customer asks ChatGPT, Perplexity, or Claude *"what's the best running shoe under $100?"* — this merchant never shows up.

**Why?** Because AI shopping agents don't rank results the same way Google does. They retrieve products by:

- Parsing structured, machine-readable data (not raw HTML)
- Matching semantic meaning, not just keywords
- Summarizing and ranking based on contextual relevance
- Relying on rich, entity-level understanding of products

A merchant with unstructured product pages, no JSON-LD schema, and keyword-stuffed descriptions is essentially invisible to these agents — regardless of their SEO score.

## How a Merchant Would Use This

- Export or stream their catalog (via Shopify API) into this backend.
- Generate structured JSON, summaries, and embeddings for all products.
- Expose this as an API/feed that AI agents or on-site AI search can query for ranked, explainable product results.

---

## What This Project Does

This project simulates the full AI product discovery pipeline — from raw product data to ranked AI retrieval — and demonstrates concretely how a merchant can go from invisible to discoverable.

It does this by building two parallel pipelines side-by-side:

**Baseline** → how AI agents currently process a typical Shopify store (poorly)

**Enhanced** → how the same products look after structured extraction, LLM summarization, and embedding-based semantic retrieval

The improvement in ranking quality between the two pipelines is the core output.

---

## How It Works

```
Raw Product Data (JSON)
         │
         ├──────────────────────────┐
         ▼                          ▼
  BASELINE PIPELINE          ENHANCED PIPELINE
  ─────────────────          ─────────────────
  Keyword matching           Structured Extraction
  (title + price only)       (category, use_case, features)
                                     │
                             Query Understanding
                             (synonym expansion,
                              intent normalization)
                                     │
                             LLM Summarization
                             (human-readable product summary
                              via OpenAI)
                                     │
                             Embedding Generation
                             (semantic vector per product)
                                     │
                             Cosine Similarity Retrieval
                                     │
         ▼                          ▼
  Weak, keyword-matched      Ranked, semantically relevant
  results                    results — AI-agent ready
```

---

## What Was Built

### Structured Extraction (`structured_extractor.py`)
Parses raw product titles and descriptions using spaCy to extract structured fields: `category`, `use_case`, and `features`. Fully domain-agnostic — works for any product type, not just a single category. This mirrors what JSON-LD schema markup does for web crawlers, but applied at inference time.

### Query Understanding (`query_understanding.py`)
Normalizes and expands user queries before retrieval. Maps synonyms and intent signals (e.g. "marathon" → "running", "office wear" → "formal") so that products rank correctly even when the user's phrasing doesn't match the product's exact wording. This is the same kind of query rewriting used by AI search engines internally.

### LLM-based Enhancer (`enhancer.py`)
Calls OpenAI to generate concise, structured summaries for each product. The output is a clean natural-language description of what the product is and who it's for — the kind of context that makes an AI agent confident enough to cite a product in a response.

### Semantic Retrieval (`semantic_retriever.py`)
Converts product descriptions to embedding vectors and ranks them against incoming queries using cosine similarity. Replaced an earlier TF-IDF implementation. This is the retrieval mechanism closest to how RAG-based AI agents actually surface products.

### Baseline vs Enhanced Comparison (`main.py`)
Runs both pipelines against the same queries and prints ranked results side-by-side, showing the concrete improvement in product visibility.

---

## Project Structure

```
polymath_test/
│
├── src/
│   ├── main.py                  # Entry point; runs and compares both pipelines
│   ├── scraper.py               # Product data loading
│   ├── parser.py                # Raw data parsing
│   ├── structured_extractor.py  # spaCy-based structured field extraction
│   ├── query_understanding.py   # Query normalization and expansion
│   ├── enhancer.py              # LLM-based product summarization
│   ├── semantic_retriever.py    # Embedding + cosine similarity retrieval
│   └── embeddings.py            # Embedding utilities
│
├── data/
│   └── sample_products.json     # Sample Shopify-style product dataset
│
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
git clone https://github.com/Shreyas200188/polymath_test.git
cd polymath_test

python3 -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate

pip install -r requirements.txt  # installs spaCy model automatically
```

Set your OpenAI API key:
```bash
# Mac/Linux
export OPENAI_API_KEY="your_api_key_here"

# Windows (PowerShell)
$env:OPENAI_API_KEY="your_api_key_here"
```

Run the pipeline:
```bash
python src/main.py
```

---

## Example Output

```
Query: "lightweight running shoes for marathon training"

── BASELINE RESULTS ──────────────────────────────
1. Nike Air Max 270        $130
2. Adidas Stan Smith       $85
3. Puma Suede Classic      $75

── ENHANCED RESULTS ──────────────────────────────
1. Nike Pegasus 40         $120   [use_case: running, features: lightweight, cushioned]
   Summary: A long-distance running shoe built for high mileage with responsive
   foam and breathable upper. Ideal for marathon and half-marathon training.

2. Brooks Ghost 15         $140   [use_case: running, features: neutral support, durable]
   Summary: A neutral daily trainer suited for marathon prep, offering soft
   landings and consistent mileage performance.

3. New Balance Fresh Foam  $110   [use_case: running, features: plush, road-ready]
   Summary: Cushioned road shoe for endurance runners seeking comfort over
   long distances.
```

The baseline surfaces shoes alphabetically by loose keyword match. The enhanced pipeline returns shoes that are semantically relevant to marathon training — the kind of result an AI agent would actually cite.

---

## Dependencies

| Library | Purpose |
|---|---|
| `openai` | LLM summarization and embeddings |
| `spacy` + `en_core_web_sm` | Structured feature extraction |
| `nltk` | Text preprocessing |
| `numpy` | Cosine similarity computation |
| `python-dotenv` | API key management |
| `requests` | HTTP utilities |

---

## Future Improvements

- Real Shopify API integration to pull live product data
- JSON-LD schema generator: output merchant-ready structured markup to embed in Shopify store HTML
- Multi-merchant benchmarking across product categories
- External signal integration (reviews, Reddit mentions, social proof)
- `llms.txt` generation for direct AI agent crawling compatibility

---

## Why This Matters

Traditional SEO optimizes for how search engine crawlers rank pages. But AI agents don't rank pages — they retrieve and synthesize *information*. A product that isn't structured, summarized, and semantically indexed is as invisible to an AI agent as a page with no title tag is to Google.

This project is a working prototype of the pipeline a merchant would need to make their products AI-discoverable — not someday, but right now, using the same mechanisms today's AI shopping agents rely on.

## Thought Process — Start to End

### Why is a good merchant invisible?

My first instinct was to look at how AI agents actually retrieve products. Tools like ChatGPT Shopping and Perplexity aren't doing Google-style ranking — they're doing retrieval-augmented generation. They pull structured, semantically rich chunks of text and reason over them. A Shopify store with raw HTML and keyword-stuffed descriptions gives those agents almost nothing to work with.

### Simulating the retrieval pipeline

Rather than building a UI or a Shopify plugin, I wanted to go one layer deeper — actually model how an AI agent ingests and ranks product data, and show what happens when you improve the input. That meant building two pipelines in parallel: one that works like a naive crawler today, and one that produces the kind of data an AI agent actually prefers.

### Building it in layers

I started simple — just keyword matching on titles and prices. That became the baseline. Then I added spaCy to extract structured fields from descriptions, because the first thing an AI agent needs is to understand what a product *is* and *who it's for*, not just what it's called. Then I added query understanding, because users don't search in catalog language — "marathon shoes" and "road running footwear" mean the same thing, but a keyword matcher treats them as completely different. Then I brought in OpenAI to generate product summaries, because an AI agent won't cite a product it can't contextualize. And finally I replaced TF-IDF with embedding-based cosine similarity, which is the closest approximation to how RAG retrieval actually works.

### Every step maps back to the original problem

| Gap | Fix |
|---|---|
| No structured data | Structured extraction via spaCy |
| Query phrasing mismatch | Query normalization and expansion |
| No context for AI to cite | LLM-generated product summaries |
| Keyword retrieval misses semantic matches | Embedding-based cosine similarity |

---

## Given More Time

### 1. JSON-LD Schema Generator
The most direct real-world output. Instead of just improving retrieval internally, generate merchant-ready JSON-LD markup they can drop straight into their Shopify theme. That's what actually makes them visible to AI crawlers at the source — before any retrieval even happens.

### 2. `llms.txt` File Generator
There's an emerging standard, similar to `robots.txt`, that tells AI agents directly what a site is about and what its best content is. Auto-generating this from the enriched product data means agents crawling the site get a clean, structured index immediately.

### 3. Real Shopify API Integration
Right now the pipeline runs on sample JSON. Connecting it to the live Shopify API means a merchant can run this on their actual catalog, with automatic re-enrichment whenever a product is added or updated.

### 4. Benchmarking Across Multiple Merchants
The demo shows one merchant improving. The real proof would be: across 10 merchants in the same category, the ones running this pipeline appear in AI results X% more often than those who don't. That's the number that makes the business case undeniable.

### 5. An Actual AI Agent Test Harness
Instead of simulating retrieval internally, pipe enriched product data directly into a real ChatGPT or Perplexity query and measure whether the merchant actually gets cited. Closing that loop turns this from a simulation into a measurable product.

### 6. External Signal Integration
Incorporate reviews, social proof, and Reddit mentions as additional ranking signals. AI agents weight trust and community validation heavily — a product with 200 five-star reviews and organic Reddit discussion should rank above an identical product with none, and right now the pipeline doesn't capture that.

### 7. Richer Query Understanding
The current synonym and intent map is hand-crafted and narrow. Replacing it with a larger database — or training a small intent classifier — would make query expansion work across any product category without manual upkeep.

### 8. Extended LLM Usage
Beyond summaries, use the LLM to generate product comparisons ("vs. competitor X"), AI-friendly metadata tags, and rich search snippets. These are the formats AI agents most readily pull into a response, so producing them directly maximizes the chance of a merchant getting cited.
