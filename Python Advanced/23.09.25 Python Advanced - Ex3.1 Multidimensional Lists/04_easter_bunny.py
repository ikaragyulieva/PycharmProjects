# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# In the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions, you should not consider the fields after the trap in
# this direction. The bunny can move within the field and cannot go outside its boundaries.
# Do not consider negative indices as valid ones. For more clarifications, see the examples below.
# Note: In some directions, the collected eggs can happen to be zero or a negative number.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected
# Constraints
# •	There will NOT be two or more paths consisting of the same total amount of eggs.
def is_in_range(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
matrix = []
bunny = []

for r in range(n):
    matrix.append([i for i in input().split(' ')])
    for c in range(n):
        if matrix[r][c] == 'B':
            bunny = [r, c]

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs = float('-inf')
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    current_eggs = 0
    current_eggs_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while is_in_range(row, col, n):
        if matrix[row][col] == 'X':
            break

        current_eggs += int(matrix[row][col])
        current_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if current_eggs > max_eggs and current_eggs_matrix:
        max_eggs = current_eggs
        max_direction = direction
        max_eggs_matrix = current_eggs_matrix

print(max_direction)
[print(x)for x in max_eggs_matrix]
print(max_eggs)



