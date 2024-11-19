def reverse_file_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(reversed(lines))

reverse_file_lines('input.txt', 'output.txt')