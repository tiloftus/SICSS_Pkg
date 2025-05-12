def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())

def get_top_n_words(texts, n=5):
    """Return the top n most common words in a list of texts."""
    from collections import Counter
    all_words = " ".join(texts).split()
    return Counter(all_words).most_common(n)
