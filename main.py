def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print_report(word_count, character_count)

def count_characters(text):
    text = text.lower()
    character_dictionary = {}
    for character in text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def print_report(word_count, character_count):
    print("--- Begin report of books/frankenstein txt ---")
    print(f"{word_count} words found in the document")
    for character in character_count:
        if character.isalpha():
            print(f"The '{character}' character was found {character_count[character]} times")
    print("--- End report ---")

main()
