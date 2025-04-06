def get_num_words(text):
    words_list = text.split()
    return len(words_list)


def get_num_chars(text):
    unique_characters = {}
    for char in text.lower():
        if char not in unique_characters:
            unique_characters[char] = 1
        else:
            unique_characters[char] += 1
    return unique_characters


def sort_on(dict):
    return dict['count']

def sorted_dicts(dict_chars):
    char_list = []
    for k,v in dict_chars.items():
        new_dict = {
            "char": k,
            "count": v
        }
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list