def replace_word_in_content(content, old_word, new_word):
    return content.replace(old_word, new_word)

find_word = input("Enter the word to find: ")
replace_word = input("Enter the word to replace it with: ")

with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()

new_content = replace_word_in_content(content, find_word, replace_word)

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(new_content)

print(f"The word '{find_word}' has been replaced with '{replace_word}' in the output file.")
