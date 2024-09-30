def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        word_count = count_words(file_contents)
        print(word_count)

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

main()