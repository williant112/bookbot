# Function to get the number of words from a string
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to count characters in a string and store it to a dict
def count_chars(text):
    letters = {}
    for char in text:
        # Lower the chars so both uppercase and lowercase is counted as the same char
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

# Functions to convert dict to list and then sort it based on num
def sort_num(dictionary):   #Helper function
    return(dictionary["num"])

def sortNconv_dict_list(dictionary):
    conv_list = []
    for key in dictionary:
        conv_list.append({"char": key, "num": dictionary[key]})
    conv_list.sort(reverse=True, key=sort_num)
    return conv_list