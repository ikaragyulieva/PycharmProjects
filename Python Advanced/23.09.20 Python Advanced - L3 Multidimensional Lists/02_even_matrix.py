# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
# Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix.
# On the next rows, you will get elements for each column separated with a comma and a space ", ".

# row = int(input())
# matrix = []
#
# for row_index in range(row):
#     elements = [int(el) for in input().split(", ")]
#     matrix.append(elements)
#
# print(matrix)
# even_matrix = []
#
# for row_index in range(row):
#     even_matrix.append([])
#     for col_index in range(len(matrix[row_index])):
#         current_element = matrix[row_index][col_index]
#         if current_element% 2 == 0:
#             even_matrix[row_index].append(current_element)
#
# print(even_matrix)

# Optimised solution:

row = int(input())
matrix = []

for row_index in range(row):
    elements = [int(el) for el in input().split(", ") if int(el) % 2 ==0]
    matrix.append(elements)

print(matrix)
