book_path = "./books/frankenstein.txt"

def main():      
    book_content = get_book_text(book_path)
    print(book_content)

def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
    return book

main()