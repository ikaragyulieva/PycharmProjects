# Everybody remembers the old mines game. Now it is time to create your own.
# You will be given an integer n for the size of the mines field with square shape and another one for the number of
# bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate
# the numbers in each cell of the field. Each cell represents a number of all bombs directly near it
# (up, down, left, right and the 4 diagonals).
# •    On the first line, you are given the integer n – the size of the square matrix.
# •    On the second line – the number of the bombs.
# •    The next n lines holds the position of each bomb.
# Output
# •	Print the matrix you've created.
# Constraints
# •	The size of the square matrix will be between [2…15].
def is_in_range(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def number_value_def(row, col, directions, matrix):
    mines_count = 0
    for direction_row, direction_col in directions:
        current_row = row + direction_row
        current_col = col + direction_col
        if not is_in_range(current_row, current_col, board_size):
            continue
        if matrix[current_row][current_col] == '*':
            mines_count += 1
    return mines_count


board_size = int(input())
mines_num = int(input())
board = []

possible_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]

for r in range(board_size):
    board.append([])
    for c in range(board_size):
        board[r].append(0)

for mine in range(mines_num):
    mine_row, mine_col = (int(el) for el in input().strip('()').split(', '))
    board[mine_row][mine_col] = '*'

for r in range(board_size):
    for c in range(board_size):
        if board[r][c] == '*':
            continue
        board[r][c] = number_value_def(r, c, possible_directions, board)

[print(*el, sep=' ') for el in board]

# Link to Judge: https://judge.softuni.org/Contests/Practice/Index/2463#1
# --- Tests: ---
# Test1:
# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)
#
# Test2:
# 5
# 3
# (1, 1)
# (2, 4)
# (4, 1)
#
# --- Outputs: ---
# Test1:
# 1 1 2 *
# 1 * 3 2
# 2 3 * 1
# * 2 1 1
#
# Test2:
# 1 1 1 0 0
# 1 * 1 1 1
# 1 1 1 1 *
# 1 1 1 1 1
# 1 * 1 0 0
