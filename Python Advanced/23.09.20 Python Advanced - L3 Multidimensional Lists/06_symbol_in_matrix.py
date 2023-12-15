# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix.
# Each row consists of ASCII characters. After that, you will receive a symbol.
# Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
# You should start searching from the top left.
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".

n = int(input())

matrix = []
for row in range(n):
    matrix.append([el for el in input()])

searched_element = input()
position = None
for row in range (n):
    if position:
        break
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_element:
            # print(f"({row}, {col})")
            position = (row, col)
            break

if not position:
    print(f"{searched_element} does not occur in the matrix")
else:
    print(position)
