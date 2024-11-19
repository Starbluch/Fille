def count_words_starting_with(words, letter):
    return sum(1 for word in words if word.lower().startswith(letter))

symbol = input("Enter the letter: ").lower()

with open('input.txt', 'r', encoding='utf-8') as infile:
    words = infile.read().split()

count = count_words_starting_with(words, symbol)
print(f"The number of words that begin with '{symbol}': {count}")