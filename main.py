import sys
from stats import get_word_count, get_char_count, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) ==2:
        text = get_book_text(sys.argv[1])
        word_count = get_word_count(text)
        character_count = get_char_count(text)
        sort_char = sort_char_dict(character_count)
        print(f"============ BOOKBOT ============ \nAnalyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dictionary in sort_char:
            if dictionary["char"].isalpha():
                print(f"{dictionary['char']}: {dictionary['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()