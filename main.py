def copy_file_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(infile.read())

copy_file_content('input.txt', 'output.txt')