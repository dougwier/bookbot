from stats import get_book_wc, get_book_cc

def main():
    file_path = "./books/frankenstein.txt"
    with open(file_path) as f:
        file_c = f.read()
    get_book_wc(file_c)
    get_book_cc(file_c)

if __name__ == "__main__":
    main()
