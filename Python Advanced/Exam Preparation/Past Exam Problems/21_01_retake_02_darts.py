# Two players bare-handed throw small sharp-pointed missiles known as darts at a round target known as a dartboard.
# Who is going to win this game?
# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# Each of the two players start with a score of 501, and they take turns to throw a dart – one throw for each player.
# The score for each turn is deducted from the player’s total score.
# The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line.
# The coordinate information of a hit will be in the format: "({row}, {column})".
# •	If a player hits outside the dartboard, he does not score any points.
# •	If a player hits a number, it is deducted from his total.
# •	If a player hits a "D" the sum of the 4 corresponding numbers per column and row
# is doubled and then deducted from his total.
# •	If a player hits a "T" the sum of the 4 corresponding numbers per column and row
# is tripled and then deducted from his total.
# •	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points, and
# they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# •	The name of the first player and the name of the second player, separated by ", "
# •	7 lines – the dartboard (separated by single space)
# •	On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# •	You should print only one line containing the winner and his count of throws:
#     "{name} won the game with {count_turns} throws!"
# Constrains
# •	There will always be exactly 7 lines
# •	There will always be a winner
# •	The points will be in range [1, 24]
# •	The coordinates will be in range [0, 100]
import math


def is_in_range(row, col, range_to_check):
    return 0 <= row < range_to_check and 0 <= col < range_to_check


def direction_count(current_row, current_col, matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    score = 0
    for direction in directions:
        for i in range(1, 7):
            row_index = current_row + direction[0] * i
            col_index = current_col + direction[1] * i
            if not is_in_range(row_index, col_index, board_range):
                break

            if matrix[row_index][col_index] not in 'B,T,D':
                score += int(matrix[row_index][col_index])
                break
    return score


first_player_name, second_player_name = input().split(', ')
board_range = 7
board = [[el for el in input().split(' ')]for row in range(board_range)]
first_player = 0
second_player = 0
throws = 0
ongoing_game = True


while ongoing_game and first_player <= 501 and second_player <= 501:
    shooting_row, shooting_col = [int(x) for x in input().strip('()').split(',')]
    throws += 1
    score_count = 0
    if not is_in_range(shooting_row, shooting_col, board_range):
        continue

    if board[shooting_row][shooting_col] == 'D':
        score_count += (direction_count(shooting_row, shooting_col, board)) * 2
    elif board[shooting_row][shooting_col] == 'T':
        score_count += (direction_count(shooting_row, shooting_col, board)) * 3
    elif board[shooting_row][shooting_col] == 'B':
        ongoing_game = False
        break
    else:
        score_count += int(board[shooting_row][shooting_col])

    if throws % 2 == 0:
        second_player += score_count
    else:
        first_player += score_count

if throws % 2 == 0:
    print(f"{second_player_name} won the game with {math.ceil(throws / 2)} throws!")
else:
    print(f"{first_player_name} won the game with {math.ceil(throws / 2)} throws!")


# --- Tests ---
# Test1:
# Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)
#
# Test2:
# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)

# --- Outputs: ---
# Test1:
# Ivan won the game with 1 throws!
#
# Test2:
# Hristo won the game with 4 throws!
