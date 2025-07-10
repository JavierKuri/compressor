import ast
import pickle
import os
import re

# Split text into words, whitespace, or punctuation tokens
def tokenize(text):
    pattern = r'(\w+|\s+|[^\w\s]+)'
    tokens = re.findall(pattern, text)
    return tokens

# Counter for frequencies of each word/token
def word_counter(text):
    counter = {}
    tokens = tokenize(text)
    for token in tokens:
        if token in counter:
            counter[token] += 1
        else:
            counter[token] = 1
    return counter

# Sort dictionary by frequency values descending
def by_value(item):
    return item[1]

def sort_dict_by_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=by_value, reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

# Create code assigning smaller integers to most frequent words
def create_code(dictionary):
    code = {}
    i = 0
    for key in dictionary:
        code[key] = i
        i += 1
    return code

# Compress to binary file 
def compress_to_binary_file(text, dictionary, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tokens = tokenize(text)
    encoded = []
    for token in tokens:
        if token in dictionary:
            encoded.append(dictionary[token])
        else:
            encoded.append(token)

    with open(filename, "wb") as f:
        pickle.dump((dictionary, encoded), f)

# Decompress from binary file
def decompress_from_binary_file(filename):
    with open(filename, "rb") as f:
        dictionary, encoded = pickle.load(f)
    reverse_code = {v: k for k, v in dictionary.items()}

    decompressed_words = []
    for token in encoded:
        if isinstance(token, int):
            decompressed_words.append(reverse_code[token])
        else:
            decompressed_words.append(token)

    return "".join(decompressed_words)