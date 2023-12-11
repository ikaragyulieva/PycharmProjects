# 1. Reverse Strings
# Write a program that:
# · Reads an input string
# · Reverses it using a stack
# · Prints the result back on the console

# Solution 1
# word = input()
#
# print(word[::-1])

# Solution 2
# word = list(input())
#
# while word:
#     print(word.pop(), end='')

# Solution 3
text = list(input())
stack = []
for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))