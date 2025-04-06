from stats import get_num_words, get_num_chars, sorted_dicts
import sys

# Remove any hard coded book paths from your code.
# At the beginning of main.py, import the built-in sys module.
# If sys.argv doesn't have two entries:
# Print a message explaining how to use the program: Usage: python3 main.py <path_to_book>
# Exit the program with a status code of 1 using sys.exit(1)
# Use the second argument in sys.argv as the path to the book file.


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    sorted_chars = sorted_dicts(get_num_chars(text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")



main()