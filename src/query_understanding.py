def normalize_query(query):
    query = query.lower()

    # simple intent mapping (this is your "AI layer")
    intent_map = {
        "marathon": "running",
        "long distance": "running",
        "jogging": "running",
        "office": "formal",
        "business": "formal"
    }

    expanded_terms = []

    for word in query.split():
        if word in intent_map:
            expanded_terms.append(intent_map[word])
        expanded_terms.append(word)

    return " ".join(expanded_terms)