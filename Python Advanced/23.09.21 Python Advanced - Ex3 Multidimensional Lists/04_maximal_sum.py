# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of
# its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" –
# integers in the range [1, 20]
# •	On the following lines, you will receive each row with its columns - integers,
# separated by a single space in the range [-20, 20]
# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a single space

rows, columns = (int(x) for x in input().split())
matrix = [[int(el) for el in input().split()]for _ in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0

        # current_sum += matrix[row][column] + matrix[row][column+1] + matrix[row][column+2] + \
        #                matrix[row+1][column] + matrix[row+1][column+1] + matrix[row+1][column+2] + \
        #                matrix[row+2][column] + + matrix[row+2][column+1] + + matrix[row+2][column+2]

        for r in range(row, row + 3):
            for c in range(column, column + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_col = column

print(f"Sum = {max_sum}")
max_sub_matrix = [matrix[r][max_col: max_col+3]for r in range(max_row, max_row + 3)]
[print(*row)for row in max_sub_matrix]

