from parser import load_products
from retriever import retrieve_products
from structured_extractor import structure_products
from structured_retriever import structured_retrieve
from query_understanding import normalize_query


def run_query(query):
    products = load_products()
    structured = structure_products(products)

    # NEW: normalize query
    normalized_query = normalize_query(query)

    baseline_results = retrieve_products(query, products)
    structured_results = structured_retrieve(normalized_query, structured)

    print(f"\nORIGINAL QUERY: {query}")
    print(f"NORMALIZED QUERY: {normalized_query}")

    print("\nBASELINE RESULTS:")
    for i, product in enumerate(baseline_results, 1):
        print(f"{i}. {product['title']} (${product['price']})")

    print("\nENHANCED RESULTS:")
    for i, product in enumerate(structured_results, 1):
        print(f"{i}. {product['name']} (${product['price']})")


if __name__ == "__main__":
    run_query("comfortable running shoes")
    run_query("formal shoes")
    run_query("trail running")
    run_query("best shoes for marathon")