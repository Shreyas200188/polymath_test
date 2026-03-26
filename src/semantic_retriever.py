from embeddings import compute_idf, compute_tfidf, cosine_similarity


def build_corpus(structured_products):
    docs = []
    for p in structured_products:
        text = f"{p['name']} {p['category']} {p['use_case']} {' '.join(p['features'])} {p['raw_description']}"
        docs.append(text)
    return docs


def semantic_retrieve(query, structured_products):
    corpus = build_corpus(structured_products)

    idf = compute_idf(corpus)

    product_vectors = [
        compute_tfidf(doc, idf) for doc in corpus
    ]

    query_vec = compute_tfidf(query, idf)

    scored = []
    for i, product in enumerate(structured_products):
        sim = cosine_similarity(query_vec, product_vectors[i])
        scored.append((sim, product))

    scored.sort(key=lambda x: x[0], reverse=True)

    # keep top 3 only
    return [p for score, p in scored[:3] if score > 0]