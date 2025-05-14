def get_book_wc(book_text):
    num_lines = len(book_text.split())
    return num_lines

def get_book_cc(book_text):
    lower_book_text = book_text.lower()
    char_counts = {}
    for chars in lower_book_text:
        if chars in char_counts:
            char_counts[chars] += 1
        else:
            char_counts[chars] = 1
    return char_counts

def sort_on(dict):
    return dict['num']

def sort_char_list(char_counts):
    sorting_a = []
    temp_dict = {}
    for k in char_counts:
        temp_dict.clear()
        if k.isalpha():
            sorting_a.append({"letter": k, "num": char_counts[k]})
    sorting_a.sort(reverse=True, key=sort_on)
    return sorting_a
