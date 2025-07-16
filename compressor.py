import pickle
import os
import re
import math

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

# Helper to calculate bits needed to represent n tokens
def bits_needed(n):
    return max(1, math.ceil(math.log2(n)))

# Bitwise compression
def compress_to_binary_file(text, dictionary, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tokens = tokenize(text)
    encoded = [dictionary[token] for token in tokens]
    max_index = max(dictionary.values())
    bits_per_token = bits_needed(max_index + 1)
    bit_string = ''
    for index in encoded:
        bit_string += format(index, f'0{bits_per_token}b')
    padding = (8 - len(bit_string) % 8) % 8
    bit_string += '0' * padding

    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = int(bit_string[i:i+8], 2)
        byte_array.append(byte)
    with open(filename, "wb") as f:
        pickle.dump((dictionary, bits_per_token, padding), f)
        f.write(byte_array)

# Bitwise decompression
def decompress_from_binary_file(filename):
    with open(filename, "rb") as f:
        dictionary, bits_per_token, padding = pickle.load(f)
        byte_data = f.read()
    reverse_code = {v: k for k, v in dictionary.items()}
    bit_string = ''.join(format(byte, '08b') for byte in byte_data)
    if padding:
        bit_string = bit_string[:-padding]
    tokens = []
    for i in range(0, len(bit_string), bits_per_token):
        bit_chunk = bit_string[i:i+bits_per_token]
        index = int(bit_chunk, 2)
        tokens.append(reverse_code[index])
    return ''.join(tokens)