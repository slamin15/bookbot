from stats import get_num_words, get_chars_dict, sorted_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = sorted_chars(chars_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars_list:
        letter = None
        num = None
        if dict['char'].isalpha():
            letter = dict['char']
            num = dict['num']

            print(f'{letter}: {num}')
    print("============= END ===============")


main()
