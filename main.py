import sys
from stats import *

# Function to read a file and return the strings contained within it
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Main function
def main():
    # Check for the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Calling functions to analyze the books
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    letters = count_chars(text)
    sorted_letters = sortNconv_dict_list(letters)
    
    # Print the report
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


# Call main()
main()

