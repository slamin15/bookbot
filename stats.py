def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_chars(chars):
    list_of_chars = []
    for key in chars:
        new_dict = {"char": key, "num": chars[key]}
        list_of_chars.append(new_dict)
    
    def sort_on(dict):
        return dict["num"]
    
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars