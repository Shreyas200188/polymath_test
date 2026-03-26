# structured_extractor.py
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_structure(product):
    """
    Extract structured information and generate summary using LLM.
    Works for any product type.
    """
    prompt = f"""
    Extract structured info from this product in JSON format:
    Title: {product['title']}
    Description: {product['description']}
    
    JSON keys:
    - category (general product type, e.g., running shoes, formal shoes, electronics)
    - use_case (primary usage, e.g., running, formal, hiking)
    - features (list of key features/adjectives)
    - summary (one concise sentence describing the product)
    """
    try:
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        structured = resp.choices[0].message.content.strip()
        return json.loads(structured)
    except Exception as e:
        print(f"LLM fallback for {product['title']}: {e}")
        # fallback minimal structure
        return {
            "id": product["id"],
            "name": product["title"],
            "price": product["price"],
            "category": "general",
            "use_case": "general",
            "features": [],
            "raw_description": product["description"],
            "summary": product["description"]
        }

def structure_products(products):
    return [extract_structure(p) for p in products]