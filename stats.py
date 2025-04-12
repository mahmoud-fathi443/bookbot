def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}

    for c in text:
        if c.lower() in char_dict:
            char_dict[c.lower()] =  char_dict[c.lower()] + 1
        else:
            char_dict[c.lower()] = 1

    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key,"count": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
    
        

