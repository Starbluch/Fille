def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

lines = read_lines('input.txt')
write_lines('output.txt', lines[:-1])