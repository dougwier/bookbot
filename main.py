from stats import get_book_wc, get_book_cc, sort_char_list

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_wc(text)
    chars_dict = get_book_cc(text)
    sort_dict = sort_char_list(chars_dict)
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
