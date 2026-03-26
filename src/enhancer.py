def generate_summary(product):
    """
    Generate a clean, concise product summary (simulating an LLM).
    """
    name = product["name"]
    category = product["category"]
    features = ", ".join(product["features"]) if product["features"] else "no special features"
    use_case = product["use_case"]

    return f"{name} is a {category} designed for {use_case}. Key features include {features}."
    

def enhance_products(structured_products):
    """
    Add a 'summary' field to each structured product.
    """
    for p in structured_products:
        p["summary"] = generate_summary(p)
    return structured_products