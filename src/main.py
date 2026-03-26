# main.py
from parser import load_products
from structured_extractor import structure_products
from retriever import retrieve_products
from structured_retriever import structured_retrieve
from semantic_retriever import semantic_retrieve
from query_understanding import normalize_query
from enhancer import enhance_products
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env into environment

api_key = os.getenv("OPENAI_API_KEY")
print("Current OpenAI API key:", api_key)

def run_query(query):
    products = load_products()
    
    # LLM-enhanced structured products
    structured = structure_products(products)
    structured = enhance_products(structured)  # optional: adds improved summaries
    
    normalized_query = normalize_query(query)
    
    baseline_results = retrieve_products(query, products)
    structured_results = structured_retrieve(normalized_query, structured)
    semantic_results = semantic_retrieve(normalized_query, structured)
    
    print(f"\nORIGINAL QUERY: {query}")
    print(f"NORMALIZED QUERY: {normalized_query}")
    
    print("\nBASELINE RESULTS:")
    for i, product in enumerate(baseline_results, 1):
        print(f"{i}. {product['title']} (${product['price']})")
    
    print("\nSTRUCTURED RESULTS:")
    for i, product in enumerate(structured_results, 1):
        print(f"{i}. {product['name']} (${product['price']}) - {product['summary']}")
    
    print("\nSEMANTIC RESULTS (Embeddings + Cosine Similarity):")
    for i, product in enumerate(semantic_results, 1):
        print(f"{i}. {product['name']} (${product['price']}) - {product['summary']}")

if __name__ == "__main__":
    run_query("comfortable running shoes")
    run_query("formal shoes")
    run_query("trail running")
    run_query("best shoes for marathon")