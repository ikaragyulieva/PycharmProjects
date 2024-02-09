# You are playing a game, and your goal is to collect 100 coins.
# On the first line, you will be given a number representing the size of the field with a square shape.
# On the following few lines, you will be given the field with:
# •	One player - randomly placed in it and marked with the symbol "P"
# •	Numbers for coins placed at different positions of the field
# •	Walls marked with "X"
# After the field state, you will be given commands for the player's movement.
# Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across.
# If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
# •	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
# •	The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
# •	A number representing the size of the field (matrix NxN)
# •	A matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will get a move command.
# Output
# •	If the player won the game, print: "You won! You've collected {total_coins} coins."
# •	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# •	Collected coins have to be rounded down to the next-lowest number.
# •	The player's path as coordinates in lists on separate lines:
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"
# Constrains
# •	There will be no case in which less than 100 coins will be in the field
# •	All given numbers will be valid integers in the range [0, 100]
import math


def is_in_range(r, c, field_range):
    return 0 <= r < field_range and 0 <= c < field_range


n = int(input())
field = []
player = []
collected_coins = 0
path_passed = []
game_ongoing = True

for row in range(n):
    field.append(input().split(' '))
    for column in range(n):
        if field[row][column] == 'P':
            player = [row, column]
            path_passed.append(player)

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while game_ongoing:
    command = input()
    for direction in directions.items():
        if command == direction[0]:
            next_row = player[0] + direction[1][0]
            next_column = player[1] + direction[1][1]

            if not is_in_range(next_row, next_column, n):
                next_row = player[0] - (direction[1][0] * (n-1))
                next_column = (player[1] - (direction[1][1]) * (n-1))

            if field[next_row][next_column] == 'X':
                collected_coins = math.floor(collected_coins * 0.5)
                game_ongoing = False
            elif [next_row, next_column] not in path_passed:
                collected_coins += int(field[next_row][next_column])

            path_passed.append([next_row, next_column])
            player = [next_row, next_column]

            if collected_coins >= 100:
                game_ongoing = False

            break

if collected_coins >= 100:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")
print("Your path:")
[print(el) for el in path_passed]




# --- Tests: ---

# Test1:
# 5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# left
# right
# right
# up
# up
# right

# Test2:
# 8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# down
# up
# left

# --- Output ---
# Test1:
# You won! You've collected 125 coins.
# Your path:
# [3, 0]
# [3, 4]
# [3, 0]
# [3, 1]
# [2, 1]
# [1, 1]
# [1, 2]
#
# Test2:
# Game over! You've collected 0 coins.
# Your path:
# [5, 2]
# [4, 2]
# [5, 2]
# [4, 2]
# [4, 1]
