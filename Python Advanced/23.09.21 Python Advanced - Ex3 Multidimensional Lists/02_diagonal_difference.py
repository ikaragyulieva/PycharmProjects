# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.

n = int(input())

matrix = [[int(el) for el in input().split()]for _ in range(n)]

primary_diagonal = sum([matrix[row][row] for row in range(n)])
secondary_diagonal = sum([matrix[row][n-row-1]for row in range(n)])

print(abs(primary_diagonal-secondary_diagonal))

