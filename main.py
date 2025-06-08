from stats import get_word_count
from stats import get_character_count
book_path = "./books/frankenstein.txt"

def main():      
    book_content = get_book_text(book_path)
    word_count = get_word_count(get_book_text(book_path))
    print(f"{word_count} words found in the document")
    
    
def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
    return book

main()