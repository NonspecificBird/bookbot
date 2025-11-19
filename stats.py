#function that acepts text from a book as a string and returns the number of words in the string
def get_num_words(book):
    word_count = len(book.split())
    return f"Found {word_count} total words"




#function that counts every character in a book
def get_character_count(book):
    #lowercase all text
    book = book.lower()
    #splits all characters individually (wip)
    character_list = list(book)
    #character dictionary
    character_counts = {}
    for c in character_list:
        if c in character_counts:
            #should use key to add 1 to associated count
            character_counts[c] += 1
        else:
            character_counts[c] = 1
            #append to character count with a count of 1
    return character_counts


#helper function (what's it do?)
def sort_on(d):
    return d["num"]

#takes a dictionary of characters and returns a sorted list of dictionaries
def get_sorted_list(character_counts):
    char_list = []
    for c in character_counts:
        char_list.append({"char": c, "num": character_counts[c]})
    #what's this part?
    char_list.sort(reverse=True, key=sort_on)
    return char_list


