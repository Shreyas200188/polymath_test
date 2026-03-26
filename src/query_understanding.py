import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nltk.download('omw-1.4')

def expand_synonyms(word, top_n=1):
    """Return a small number of synonyms for a word using WordNet"""
    syns = wn.synsets(word)
    lemmas = set()
    for s in syns:
        for l in s.lemmas():
            l_clean = l.name().replace("_", " ")
            # avoid overly generic or unrelated words
            if len(l_clean) < 20 and l_clean.isalpha():
                lemmas.add(l_clean)
    lemmas.discard(word)
    return list(lemmas)[:top_n]

def normalize_query(query):
    query = query.lower()
    expanded_terms = []

    for word in query.split():
        expanded_terms.append(word)
        expanded_terms.extend(expand_synonyms(word))  # add generic synonyms

    return " ".join(expanded_terms)