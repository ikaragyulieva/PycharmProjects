# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# •	"." – empty square
# •	"Q" – a queen
# •	"K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move
# diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the
# knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing the
# king. For more clarification see the examples.
# Input
# •	8 lines – the state of the board (each square separated by single space)
# Output
# •	The positions of the queens that can capture the king as lists
# •	If the king cannot be captured, print: "The king is safe!"
# •	The order of output does not matter
# Constrains
# •	There will always be exactly 8 lines
# •	There will always be exactly one King
# •	Only the 3 symbols described above will be present in the input


# https://judge.softuni.org/Contests/2551/Python-Advanced-Exam-24-October-2020

def is_in_range(r, c):
    return 0 <= r < 8 and 0 <= c < 8


def direction_to_check(r, c, row_movement, col_movement, matrix):
    for i in range(1, 8):
        row_index = r + row_movement * i
        col_index = c + col_movement * i
        if not is_in_range(row_index, col_index) or matrix[row_index][col_index] == 'Q':
            break
        elif matrix[row_index][col_index] == 'K':
            return True
    return False


board = []
winning_queens = []

for _ in range(8):
    board.append([el for el in input().split(' ')])

possible_moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 1),
    (1, 1),
    (1, -1),
    (-1, -1)
]

for row in range(8):
    for col in range(8):
        if board[row][col] == 'Q':
            for move_row, move_col in possible_moves:
                if direction_to_check(row, col, move_row, move_col, board):
                    winning_queens.append([row, col])
                    break
if winning_queens:
    [print(el) for el in winning_queens]
else:
    print("The king is safe!")
