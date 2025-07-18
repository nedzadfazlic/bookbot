def get_book_num_words(path_to_file):
    with open(path_to_file) as f:
        num_words = len(f.read().split())
    return num_words

def get_character_count(path_to_file: str) -> dict[str, int]:
    
    with open(path_to_file) as f:
        character_count = f.read().lower()
    
    char_count: dict[str, int] = {}

    for char in character_count:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def sorted_list(path_to_file):
    
    print('''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...''')
    print("----------- Word Count ----------")
    num_words = get_book_num_words(path_to_file)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_character_count(path_to_file)
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")    
