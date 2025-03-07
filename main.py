import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    char_counts = count_chars(text)
    sorted_chars = sort_char_counts(char_counts)
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()