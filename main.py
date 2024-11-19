def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def compare_files(file1_lines, file2_lines):
    min_lines = min(len(file1_lines), len(file2_lines))
    for idx in range(min_lines):
        if file1_lines[idx] != file2_lines[idx]:
            print(f"Line {idx + 1} does not match:")
            print(f"File 1: {file1_lines[idx].strip()}")
            print(f"File 2: {file2_lines[idx].strip()}")

    if len(file1_lines) != len(file2_lines):
        print("\nFiles have a different number of lines.")

lines_file1 = read_lines('file1.txt')
lines_file2 = read_lines('file2.txt')
compare_files(lines_file1, lines_file2)