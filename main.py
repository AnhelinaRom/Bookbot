def main():
    # Print the whole book in console
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Count words of the whole text
    words = len(text.split())

    # Char count in text
    to_lower = text.lower()
    char_counted = character_count(to_lower)

    formatted_list = []

    for char_dict in char_counted:
        formatted_entry = f"The '{char_dict['char']}' character was found {char_dict['num']} times"
        formatted_list.append(formatted_entry)


    # A nicly formated report
    print(f"--- Begin report of {book_path} ---")
    print(f"Words count in a book: {words}")
    print(f"")
    for entry in formatted_list:
        print(entry)
    print("--- End of report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(low_text):
    char_count = {}
    for char in low_text:
        if char.isalnum():
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    
    sorted_chars = char_sort(char_count)

    return sorted_chars

# Turn dictionary into list and sort it
def char_sort(char_count):
    char_list = []

    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

main()