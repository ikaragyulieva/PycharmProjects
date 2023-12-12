# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

text = tuple(input())

unique_symbols = sorted(set(text))
for char in unique_symbols:
    print(f"{char}: {text.count(char)} time/s")
