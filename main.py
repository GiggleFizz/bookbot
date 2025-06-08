from stats import get_word_count
from stats import get_character_count
from stats import letter_sort

book_path = "./books/frankenstein.txt"

def main():      
    word_count = get_word_count(get_book_text(book_path))
    letter_counts = get_character_count(get_book_text(book_path))
    sorted_list = letter_sort(letter_counts)
    #print(f"{word_count} words found in the document")
    #print(letter_counts)
    #print(letter_list)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        alpha = item["char"]
        if alpha.isalpha():
            print(f"{alpha}: {item["num"]}")
    print("============= END ===============")
    
def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
    return book

main()