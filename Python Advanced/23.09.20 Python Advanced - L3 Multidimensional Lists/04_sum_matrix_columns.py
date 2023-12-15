# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.
# Hints
# •	Read matrix sizes.
# •	On the next row lines, read the columns.
# •	Traverse the matrix and sum all elements in each column.
# •	Print the sum and continue with the other columns.

data = input().split(", ")
rows = int(data[0])
columns = int(data[1])

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for col in range(columns):
    sum_col_nums = 0
    for row in range(rows):
        sum_col_nums += matrix[row][col]
    print(sum_col_nums)