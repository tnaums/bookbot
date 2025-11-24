import sys
from stats import count_book_words
from stats import character_count
from stats import sorted_list

def get_book_text(file):

    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_text = get_book_text(sys.argv[1])
    num_words = count_book_words(book_text)
    characters = character_count(book_text)
    sorted_characters = sorted_list(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')
    print("============= END ===============")
        
main()
