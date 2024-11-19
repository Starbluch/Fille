def swap_symbols(content, symbol1='*', symbol2='&'):
    return content.replace(symbol1, 'TEMP').replace(symbol2, symbol1).replace('TEMP', symbol2)

with open('input.txt', 'r', encoding='utf-8') as infile:
    content = infile.read()

swapped_content = swap_symbols(content)

with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(swapped_content)