def find_longest_line_length(lines):
    return max(len(line.strip()) for line in lines)

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

max_length = find_longest_line_length(lines)
print(f"The length of the longest line is: {max_length}")