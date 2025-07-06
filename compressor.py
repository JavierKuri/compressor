import sys
import ast 

def word_counter(text):
    counter = {}
    words = text.strip().split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

def by_value(item):
    return item[1]

def sort_dict_by_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=by_value, reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

def create_code(dictionary):
    code = {}
    i = 0
    for key in dictionary:
        code[key] = i
        i += 1
    return code

def create_compressed_text(text, dictionary):
    compressed = str(code) + "\n"
    words = text.split()
    for word in words:
        if word in dictionary:
            compressed += str(dictionary[word]) + " "
        else:
            compressed += word + " "
    return compressed

def get_code(compressed_text):
    code = ""
    for character in compressed_text:
        if character == "}":
            break
        else:
            code += character
    code += "}"
    return(code)

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
code = ast.literal_eval(get_code(compressed_text))

#print(sys.getsizeof(text))
#print(sys.getsizeof(compressed_text))
#print(sys.getsizeof(code))