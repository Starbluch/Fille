def count_word_occurrences(words, target_word):
    return sum(1 for word in words if word == target_word)

search_word = input("Enter the word to count: ")

with open('input.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()

count = count_word_occurrences(words, search_word)
print(f"The word '{search_word}' appears {count} times.")