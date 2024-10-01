def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print(word_count, character_count)

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    character_count = {}
    for character in text:
        character = character.lower()
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count
main()