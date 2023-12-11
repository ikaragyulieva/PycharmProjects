# You will be given a sequence consisting of parentheses.
# Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs
# after the former.
# There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# •	On a single line, you will receive a sequence of parentheses.
# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# •	Otherwise, print "NO"
# Constraints
# •	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
# •	Each character of the sequence will be one of {, }, (, ), [, ]

from collections import deque

expression = deque(input())
opening_brackets = '({['
closing_brackets = ')}]'
count = 0

while expression and count < len(expression) / 2:
    if expression[0] not in opening_brackets:
        break
    index = opening_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(count)
        count = 0
    else:
        expression.rotate(-1)
        count += 1

if expression:
    print('NO')
else:
    print('YES')
