def word_counter(text):
    counter = {}
    curr_word = ""
    for char in text:
        if char == ' ':
            if curr_word != "":
                if curr_word in counter:
                    counter[curr_word] += 1
                else:
                    counter[curr_word] = 1
                curr_word = ""
        else:
            curr_word += char
    if curr_word != "":
        if curr_word in counter:
            counter[curr_word] += 1
        else:
            counter[curr_word] = 1
    return counter

def by_value(item):
    return item[1]

def sort_dict_by_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=by_value, reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict