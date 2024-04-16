# Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.
# Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

symbols = ['-', ',', '.', '!', '?']
with open("01_text.txt", "r") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for element in symbols:
                line = line.replace(element, '@')

            print(' '.join(reversed(line.split())))




