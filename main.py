from stats import get_word_count, get_char_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():
    args = sys.argv
    if(len(args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(args[1])
    word_count = get_word_count(text)
    char_count = get_char_count(text)

    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {args[1]}\n" \
    f"Found {word_count} Total words\n" \
    "--------- Character Count -------" )
    
    char_list = sort_dict(char_count)
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")

    print("============= END ===============")

    

main()