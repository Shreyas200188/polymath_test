def structured_score(query, product):
    query = query.lower()

    score = 0

    # category match
    if product["category"] in query:
        score += 3

    # use case match
    if product["use_case"] in query:
        score += 2

    # feature match
    for feature in product["features"]:
        if feature in query:
            score += 1

    # fallback: keyword in name
    if product["name"].lower() in query:
        score += 1

    return score


def structured_retrieve(query, structured_products):
    scored = []

    for product in structured_products:
        score = structured_score(query, product)

        # fallback: weak keyword match on raw description
        if score == 0:
            if any(word in product["raw_description"].lower() for word in query.split()):
                score = 0.5

        scored.append((score, product))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [p for score, p in scored if score > 0]