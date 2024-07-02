def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_char(text)
    char_count_sorted = chars_dict_to_sorted_list(char_count)
    print_book_report(book_path,word_count,char_count_sorted)

def count_words(book):
    words = book.split()
    number_of_words = len(words)
    return number_of_words

def count_char(book):
    char_numbers = {}
    text_lower = book.lower() 
    for i in text_lower:
        if i in char_numbers:
            char_numbers[i] += 1
        else:
            char_numbers[i] = 1
    return char_numbers

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_book_report(book_path,word_count,char_count_sorted):

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_count_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

main()