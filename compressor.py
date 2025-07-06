import sys
import ast 

#Counter for getting frequencies of each word/token
def word_counter(text):
    counter = {}
    words = text.strip().split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

#Functions for ordering dictionary by frequency values
def by_value(item):
    return item[1]
def sort_dict_by_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=by_value, reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

#Creating the code by giving the smaller values to the most repeated words/tokens
def create_code(dictionary):
    code = {}
    i = 0
    for key in dictionary:
        code[key] = i
        i += 1
    return code

#Compress the given text
def create_compressed_text(text, dictionary):
    compressed = str(dictionary) + "\n"
    words = text.split()
    for word in words:
        if word in dictionary:
            compressed += str(dictionary[word]) + " "
        else:
            compressed += word + " "
    return compressed

#Get code from compressed text, as well as index where the compressed info starts
def get_code_and_closing_brace_index(compressed_text):
    code = ""
    closing_brace_index = -1
    for i in range(len(compressed_text)):
        code += compressed_text[i]
        if compressed_text[i] == "}":
            closing_brace_index = i
            break
    return code, closing_brace_index

#Decompress a compressed text
def decompress_text(compressed_text):
    decompressed_text = ""
    code_str, index = get_code_and_closing_brace_index(compressed_text)
    code_dict = ast.literal_eval(code_str)
    reverse_code = {v: k for k, v in code_dict.items()}
    remaining_text = compressed_text[index + 1:].strip().split()
    for token in remaining_text:
        if token.isdigit():
            decompressed_text += reverse_code[int(token)] + " "
        else:
            decompressed_text += token + " "
    return decompressed_text.strip()

#Example usage
text = (
    "In the world of software development, clarity and simplicity are often more valuable than cleverness. "
    "Clean code is not only easier to read, but also easier to maintain and less prone to bugs. "
    "Developers who take the time to write readable, well-structured code often save time in the long run. "
    "While performance is important, premature optimization can make code harder to understand and modify. "
    "Therefore, focusing on good design principles, writing tests, and documenting your thought process "
    "can lead to software that is both robust and adaptable."
)

counter_dict = word_counter(text)
counter_dict = sort_dict_by_values(counter_dict)
code = create_code(counter_dict)
compressed_text = create_compressed_text(text, code)
print(compressed_text)
decompressed_text = decompress_text(compressed_text)
print(decompressed_text)
print(text == decompressed_text)
#print(sys.getsizeof(text))
#print(sys.getsizeof(compressed_text))
#print(sys.getsizeof(code))