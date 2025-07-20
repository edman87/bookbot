def get_word_count(text):
    split_words = text.split()
    return len(split_words)

def get_char_count(text):
    char_dict = {}
    small_char = text.lower()
    for character in small_char:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict

def sort_char_dict(char_dict):
    char_list = []
    for char, count in char_dict.items():
        new_dict = {"char": char, "num": count}
        char_list.append(new_dict)
    def char_num(dictionary):
        return dictionary["num"]
    char_list.sort(reverse=True, key=char_num)
    return char_list
    