from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

# Count words of a string
def count_words(text):
    return len(text.split())

# Unpacks text file into a string and then runs count_words
def run_count_words_from_file(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return avg_word_length(text, n)

# Get top n words of a string- n defaults to 10
def get_top_n_words(text, n=10):
    stop_words = {'the', 'and', 'a', 'an', 'in', 'on', 'at', 'of', 'to', 'for', 
                  'with', 'that', 'is', 'was', 'as', 'by', 'it', 'this', 'from', 
                  'be', 'or', 'are', 'but', 'if', 'not', 'we', 'you', 'they', 
                  'he', 'she', 'them', 'his', 'her', 'its'}

    words = re.findall(r'\b[a-z]+\b', text.lower())

    filtered_words = [word for word in words if word not in stop_words]

    return Counter(filtered_words).most_common(n)

# Unpacks text file into a string and then runs get_top_n_words
def run_top_words_from_file(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return get_top_n_words(text, n)

# Compute the average length of each word in the text. Code it on your own!
def avg_word_length(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Unpacks text file into a string and then runs avg_word_length
def run_avg_words_from_file(filename, n=10):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return avg_word_length(text, n)