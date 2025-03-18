from stats import count_words, count_characters, sort_characters
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
        book_text = get_book_text(path_to_file=path_to_file)
        num_words = count_words(book_text)
        num_characters = count_characters(book_text)
        count_characters_dict = sort_characters(num_characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in count_characters_dict:
            if entry["character"].isalpha() == True:
                print(f"{entry["character"]}: {entry["count"]}")
            else:
                pass
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()