def get_word_count(book):
    words = book.split()
    word_count = 0
    for i in words:
        word_count += 1
    return word_count

def get_character_count(book):
    lowered_letters = book.lower()
    letter_counts = {}
    for letter in lowered_letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1    

    return letter_counts
