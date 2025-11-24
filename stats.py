def count_book_words(book_words):
    book_words_list = book_words.split()
    return len(book_words_list)

def character_count(book_text):
    character_dict = {}
    for character in book_text:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sorted_list(character_dict):
    character_list = []
    for key, value in character_dict.items():
        temp_dict = {
            "char": key,
            "num": value,
            }
        character_list.append(temp_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list
