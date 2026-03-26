import math
from collections import Counter


def tokenize(text):
    return text.lower().split()


def compute_tf(text):
    words = tokenize(text)
    tf = Counter(words)
    total = len(words)
    return {w: c / total for w, c in tf.items()}


def compute_idf(documents):
    import math
    N = len(documents)
    idf = {}

    all_words = set()
    for doc in documents:
        all_words.update(tokenize(doc))

    for word in all_words:
        containing = sum(1 for doc in documents if word in tokenize(doc))
        idf[word] = math.log(N / (1 + containing))

    return idf


def compute_tfidf(text, idf):
    tf = compute_tf(text)
    return {w: tf[w] * idf.get(w, 0) for w in tf}


def cosine_similarity(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    dot = sum(vec1[w] * vec2[w] for w in common)

    norm1 = math.sqrt(sum(v**2 for v in vec1.values()))
    norm2 = math.sqrt(sum(v**2 for v in vec2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0

    return dot / (norm1 * norm2)