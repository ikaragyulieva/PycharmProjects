# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
# separated by a comma and a space ", ". You should find the matrix's diagonals,
# prints them, and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

n = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

# Comprehension fill in matrix:
# matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

for row in range(n):
    matrix.append([int(el)for el in input().split(", ")])

# Comprehension for getting diagonals:
# primary_diagonal = [matrix[i][i] for i in range(n)]
# secondary_diagonal = [matrix[i][n-i-1]for i in range(n)]

for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][n-row-1])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")


