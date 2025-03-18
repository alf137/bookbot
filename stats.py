
#Function to count the words in the text
def count_words(text_string):
    if text_string == "":
        return 0
    else:
        words = text_string.split()
        num_words = len(words)
        return num_words
    
def count_characters(text_string):
    char_counts_dict = {}
    for char in text_string.lower():
        if char in char_counts_dict.keys():
            char_counts_dict[char] = char_counts_dict.get(char) + 1
        else: 
            char_counts_dict[char] = 1
    return char_counts_dict

def sort_on(dict):
    return dict["count"]

def sort_characters(count_characters_dict):
    list_of_dicts = [{"character":char, "count" : count} for char, count in count_characters_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts