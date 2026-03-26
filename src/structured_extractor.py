def extract_structure(product):
    title = product["title"].lower()
    description = product["description"].lower()

    category = "unknown"
    use_case = "general"
    features = []

    # very simple heuristics (intentionally basic)
    if "running" in title or "running" in description:
        category = "running shoes"
        use_case = "running"

    if "trail" in description:
        features.append("trail")

    if "comfortable" in description:
        features.append("comfort")

    if "leather" in description:
        category = "formal shoes"
        use_case = "formal"

    return {
        "id": product["id"],
        "name": product["title"],
        "price": product["price"],
        "category": category,
        "use_case": use_case,
        "features": features,
        "raw_description": product["description"]
    }


def structure_products(products):
    return [extract_structure(p) for p in products]