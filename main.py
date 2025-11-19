from stats import (get_num_words, get_character_count, get_sorted_list)
import sys



#take a file path and returns the contents as a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

#main function that uses get_book_text with the relative path to frankenstein.txt and prints to console
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    sorted_list = get_sorted_list(character_count)
    print_report(path, num_words, sorted_list)

def print_report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_list:
        if not c["char"].isalpha():
            continue
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    

#Calls main
main()