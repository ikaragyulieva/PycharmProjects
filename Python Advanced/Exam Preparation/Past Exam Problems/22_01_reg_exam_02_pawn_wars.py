# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked
# from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number
# (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# •	Only move forward in a straight line:
# 	White (w) moves from the 1st rank to the 8th rank direction.
# 	Black (b) moves from 8th rank to the 1st rank direction.
# •	Can move only 1 square at a time.
# •	Can capture another pawn in from of them only diagonally:
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one -
# this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the
# white pawn (w), then black moves (b), then white (w) again, and so on.
# Some rules apply when moving paws:
# •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures
# another pawn, the game is over.
# •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o	Empty positions are marked with "-".
# o	White pawn is marked with "w"
# o	Black pawn is marked with "b"
# Output
# Print either one of the following:
# •	If a pawn captures the other, print:
# o	"Game over! {White/Black} win, capture on {square}."
# •	If a pawn reaches the last rank, print:
# o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
# •	The input will always be valid.
# •	The matrix will always be 8x8.
# •	There will be no case where two pawns are placed on the same square.
# •	There will be no case where two pawns are placed on the same column.
# •	There will be no case where black/white will be placed on the last rank.


def is_in_range(row, col, range_to_check):
    return 0 <= row < range_to_check and 0 <= col < range_to_check


def is_captured(attacking, defending, directions):
    for direction in directions:
        checking_row = attacking[0] + direction[0]
        checking_col = attacking[1] + direction[1]
        if not is_in_range(checking_row, checking_col, BOARD_RANGE):
            continue
        if checking_row == defending[0] and checking_col == defending[1]:
            return checking_row, checking_col


BOARD_RANGE = 8
board = []
black_pawn = []
white_pawn = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

diagonals = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
game_over = False
is_queen = False
for r in range(BOARD_RANGE):
    board.append(input().split(' '))
    for c in range(BOARD_RANGE):
        if board[r][c] == 'b':
            black_pawn = [r, c]
        if board[r][c] == 'w':
            white_pawn = [r, c]

for _ in range(BOARD_RANGE):
    if is_captured(white_pawn, black_pawn, diagonals):
        position = positions_col[is_captured(white_pawn, black_pawn, diagonals)[1]] + position_row[is_captured(white_pawn, black_pawn, diagonals)[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn[0] -= 1
    if white_pawn[0] == 0:
        position = positions_col[white_pawn[1]] + position_row[white_pawn[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    if is_captured(black_pawn, white_pawn, diagonals):
        position = positions_col[is_captured(black_pawn, white_pawn, diagonals)[1]] + position_row[is_captured(black_pawn, white_pawn, diagonals)[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn[0] += 1
    if black_pawn[0] == 7:
        position = positions_col[black_pawn[1]] + position_row[black_pawn[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break

# --- Tests: ---
# Test1:
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
#
# Test2:
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - w - - - - - -
# - - - - - - - -
#
# --- Outputs: ---
# Test1:
# Game over! White pawn is promoted to a queen at b8.
# Test2:
# Game over! White win, capture on a3.
