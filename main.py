def count_characters(text):
    return len(text)

with open('input.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()

num_chars = count_characters(content)
print(f"Number of characters in the file: {num_chars}")