from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())

def get_top_n_words(text, n=10):
    # Hardcoded list of common English stop words
    stop_words = {'the', 'and', 'a', 'an', 'in', 'on', 'at', 'of', 'to', 'for', 
                  'with', 'that', 'is', 'was', 'as', 'by', 'it', 'this', 'from', 
                  'be', 'or', 'are', 'but', 'if', 'not', 'we', 'you', 'they', 
                  'he', 'she', 'them', 'his', 'her', 'its'}

    # Lowercase and remove non-alphabetic characters
    words = re.findall(r'\b[a-z]+\b', text.lower())

    # Filter out stop words
    filtered_words = [word for word in words if word not in stop_words]

    # Count and return the top N most common words
    return Counter(filtered_words).most_common(n)

def run_top_words_from_file(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return get_top_n_words(text, n)