# semantic_retriever.py
from openai import OpenAI
import os
import numpy as np
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_text(text):
    """Get embedding vector for a text"""
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(resp.data[0].embedding)

def semantic_retrieve(query, structured_products, top_k=5):
    """Return top_k products based on embedding similarity"""
    query_emb = embed_text(query)
    results = []
    for p in structured_products:
        p_emb = embed_text(p["summary"])
        sim = np.dot(query_emb, p_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(p_emb))
        results.append((sim, p))
    results.sort(reverse=True, key=lambda x: x[0])
    return [p for _, p in results[:top_k]]