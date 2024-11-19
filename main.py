def get_long_words(words, length=7):
    long_words = [word for word in words if len(word) >= length]
    return long_words, len(long_words)

with open("input.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

long_words, count_words = get_long_words(words)
print("Words at least 7 characters long:\n")
print(long_words)
print(f"\nNumber of such words: {count_words}")

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(long_words) + "\n")