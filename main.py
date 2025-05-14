import sys
from stats import get_book_wc, get_book_cc, sort_char_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_book_wc(text)
    chars_dict = get_book_cc(text)
    sort_dict = sort_char_list(chars_dict)
    print_report(book_path, num_words, sort_dict)

def print_report(book_path, num_words, sort_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_dict:
        print(f"{i["letter"]}: {i["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
