# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line,
# you will receive the matrix's dimensions in the format "{rows} {columns}".
# In the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.

rows, columns = (int(x) for x in input().split())
matrix = [[x for x in input().split()]for _ in range(rows)]

num_square_matrices = 0

for row in range(rows-1):
    for column in range(columns-1):
        current_element = matrix[row][column]
        next_element = matrix[row][column+1]
        below_element = matrix[row+1][column]
        diagonal_element = matrix[row+1][column+1]

        if current_element == next_element == below_element == diagonal_element:
            num_square_matrices += 1

print(num_square_matrices)

