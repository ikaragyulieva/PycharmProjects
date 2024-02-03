# Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
# contained in another file text.txt. Matching should be case-insensitive.
# The results should be written into other text files. Sort the words by frequency in descending order.
import re
with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", "r") as file:
    text = file.read().lower()

words = {}

for searched_word in searched_words:
    regex = f"\\b{searched_word}\\b"
    result = re.findall(regex, text)
    words[searched_word] = len(result)

with open("output.txt", "w") as file:
    for key, value in sorted(words.items(), key=lambda kvp: kvp[-1]):
        file.write(f"{key} - {value}\n")
