import ast
import pickle
import os

# Counter for frequencies of each word/token
def word_counter(text):
    counter = {}
    words = text.strip().split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
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
    words = text.split()
    encoded = []
    for word in words:
        if word in dictionary:
            encoded.append(dictionary[word])
        else:
            encoded.append(word)

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

    return " ".join(decompressed_words)