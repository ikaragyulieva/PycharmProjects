# Write a program that prints the calculated logarithm of any given number
# Input
# •	On the first line, you will receive the number (an integer)
# •	On the second line, you will receive a number, which is the logarithm base.
# It can be either a number or the word "natural"
# The output should be formatted to the 2nd decimal digit
# Hints
# Use the math module. You can read more about it here
# 1.	Import the module:
# 2.	Read the variables:
# 3.	Implement the logic:

from math import log

number = int(input())
command = input()

if command == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(command)):.2f}")


