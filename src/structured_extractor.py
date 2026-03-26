import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_structure(product):
    """
    Fully generic structured extractor for any product.
    - Detect category from most frequent noun in title + description
    - Use_case from secondary nouns if available
    - Features from adjectives
    """
    text = f"{product['title']}. {product['description']}".lower()
    doc = nlp(text)

    # Extract nouns & proper nouns as candidates for category/use_case
    nouns = [token.lemma_ for token in doc if token.pos_ in ("NOUN", "PROPN")]
    adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"]

    if nouns:
        # category = most common noun
        category = Counter(nouns).most_common(1)[0][0]
        # use_case = second most common noun if exists, else same as category
        use_case = Counter(nouns).most_common(2)[1][0] if len(Counter(nouns).most_common(2)) > 1 else category
    else:
        category = "general"
        use_case = "general"

    return {
        "id": product["id"],
        "name": product["title"],
        "price": product["price"],
        "category": category,
        "use_case": use_case,
        "features": adjectives,
        "raw_description": product["description"]
    }

def structure_products(products):
    return [extract_structure(p) for p in products]