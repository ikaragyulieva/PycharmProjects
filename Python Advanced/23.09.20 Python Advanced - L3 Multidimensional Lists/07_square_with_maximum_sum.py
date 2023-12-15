# Write a program that reads a matrix from the console and finds the 2x2 top-left
# submatrix with the biggest sum of its values.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
# Hints
# •	Be aware of IndexError
# •	If you find more than one max square, print the top-left one

rows, cols = (int(x) for x in input().split(", "))

matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float('-inf')
max_sum_sub_matrix = []

for row in range(rows-1):
    for col in range(cols-1):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        below_element = matrix[row+1][col]
        diagonal_element = matrix[row+1][col+1]
        sum_elements = current_element+next_element+below_element+diagonal_element

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [
                [current_element, next_element],
                [below_element, diagonal_element]
            ]
print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)
