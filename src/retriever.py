def keyword_match_score(query, text):
    query_words = query.lower().split()
    text = text.lower()
    
    score = 0
    for word in query_words:
        if word in text:
            score += 1
    return score


def retrieve_products(query, products):
    scored = []

    for product in products:
        text = product["title"] + " " + product["description"]
        score = keyword_match_score(query, text)
        scored.append((score, product))

    # sort by score descending
    scored.sort(key=lambda x: x[0], reverse=True)

    return [p for score, p in scored if score > 0]