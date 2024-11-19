def insert_separator(lines, separator='************'):
    inserted = False
    result = []
    for line in lines:
        result.append(line)
        if ',' not in line and not inserted:
            result.append(separator + '\n')
            inserted = True
    if not inserted:
        result.append(separator + '\n')
    return result

with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

updated_lines = insert_separator(lines)
with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(updated_lines)