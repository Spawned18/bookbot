def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        character_report(character_count, word_count)

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

def character_report(character_count, word_count):
    sorted_characters = [
        {"char": char, "num": count}
        for char, count in character_count.items() if char.isalpha()
    ]
    sorted_characters.sort(key=lambda x: x['num'], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for char_info in sorted_characters:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    print("\n--- End report ---")

main()