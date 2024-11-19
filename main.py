def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines) + "\n")

lines = ["Row 1", "Row 2", "Row 3"]
write_lines('output.txt', lines)