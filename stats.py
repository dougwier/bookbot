def get_book_wc(book_text):
    num_lines = len(book_text.split())
    print(f"{num_lines} words found in the document")

def get_book_cc(book_text):
    lower_book_text = book_text.lower()
    char_counts = {}
    for chars in lower_book_text:
        if chars in char_counts:
            char_counts[chars] = char_counts[chars] + 1
        else:
            char_counts[chars] = 1
    print(char_counts)
