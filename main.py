def count_lines(lines):
    return len(lines)

with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

num_lines = count_lines(lines)
print(f"Number of rows in the file: {num_lines}")