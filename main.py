def count_characters(content):
    return len(content)

def count_lines(content):
    return content.count('\n') + 1

def count_vowels(content):
    vowels = 'aeiou'
    return sum(1 for char in content.lower() if char in vowels)

def count_consonants(content):
    vowels = 'aeiou'
    return sum(1 for char in content.lower() if char.isalpha() and char not in vowels)

def count_digits(content):
    return sum(1 for char in content if char.isdigit())

with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

num_chars = count_characters(content)
num_lines = count_lines(content)
num_vowels = count_vowels(content)
num_consonants = count_consonants(content)
num_digits = count_digits(content)

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f"Number of characters: {num_chars}\n")
    outfile.write(f"Number of lines: {num_lines}\n")
    outfile.write(f"Number of vowels: {num_vowels}\n")
    outfile.write(f"Number of consonants: {num_consonants}\n")
    outfile.write(f"Number of digits: {num_digits}\n")