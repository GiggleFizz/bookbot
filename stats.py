def get_word_count(book):
    words = book.split()
    word_count = 0
    for i in words:
        word_count += 1
    return word_count

def get_character_count(book):
    lowered_letters = book.lower()
    letter_counts = {}
    for char in lowered_letters:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1    
    return letter_counts

def sort_on(dict):
    return dict["num"]

def letter_sort(letter_counts):
    sorted_list = []
    for char,count in letter_counts.items():
        sorted_list.append({"char": char,"num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

