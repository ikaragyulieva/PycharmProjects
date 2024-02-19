# An intern from a big company must solve the game - "The squirrel".
# He does not have enough experience, so he needs your help.
# Here are the rules of the game:
# The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
# You get as input the size of the field, which will be always a square shape.
# After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up" in a
# sequence, each value separated by a comma and a space (", "). On the next rows, you will receive the field.
# Possible characters in the field:
# •	s - represents the squirrel's position.
# •	h – represents a hazelnut.
# •	* – the asterisk represents an empty position.
# •	t – represents a trap.
# The squirrel starts from the s - position.
# •	If the squirrel steps on a hazelnut, you have to increase them by 1.
# The position should be marked with an asterisk (*).
# o	If the squirrel collects all 3 hazelnuts, the game ends.
# •	Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
# •	If it steps on a trap, the game ends.
# •	If the squirrel moves out of the field, the game ends.
# After all commands you will have 4 possible results:
# •	You win if the squirrel collects 3 of the hazelnuts.
# •	The squirrel collects less than 3 hazelnuts.
# •	The squirrel steps on a trap.
# •	The squirrel moves out of the field.
# Input
# •	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
# •	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
# •	In the next N lines, you will receive the values for every row.
# Output
# •	On the first line:
# o	If the squirrel goes out of the field - "The squirrel is out of the field.".
# o	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
# o	If the squirrel has not collected all hazelnuts - "There are more hazelnuts to collect.".
# o	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
# •	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
# Constraints
# •	The size of the field will be between [3,5].
# •	There could be one or no trap on the field.
# •	There will always be 3 hazelnuts on the field.
from collections import deque


def is_in_range(r, c, board):
    return 0 <= r < board and 0 <= c < board


def squirrel_movement(squirrel, current_command, movement_directions):
    move_row = 0
    move_col = 0
    for direction, moves in movement_directions.items():
        if current_command == direction:
            move_row = squirrel[0] + moves[0]
            move_col = squirrel[1] + moves[1]
    return move_row, move_col


n = int(input())
field = []
squirrel = []
hazelnuts = 0
commands = deque(input().split(', '))
game_over = False
for r in range(n):
    item = list(input())
    field.append(item)
    for c in range(n):
        if field[r][c] == 's':
            squirrel = r, c

possible_directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while commands and hazelnuts < 3:
    current_command = commands.popleft()
    move_row, move_col = squirrel_movement(squirrel, current_command, possible_directions)
    if not is_in_range(move_row, move_col, n):
        print("The squirrel is out of the field.")
        game_over = True
        break
    if field[move_row][move_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        game_over = True
        break
    if field[move_row][move_col] == 'h':
        field[move_row][move_col] = '*'
        hazelnuts += 1

    squirrel = move_row, move_col

if not game_over and hazelnuts == 3:
    print(f"Good job! You have collected all hazelnuts!")
elif not game_over and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")

# --- Tests: ---
# Test1:
# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*
# *****
#
# Test2:
# 4
# down, down, right, right
# *s*h
# ***h
# ***t
# h***
#
# Test3:
# 4
# down, down, right, right
# h***
# ***h
# *s*t
# **h*
#
# --- Outputs: ---
# Test1:
# Good job! You have collected all hazelnuts!
# Hazelnuts collected: 3
#
# Test2:
# Unfortunately, the squirrel stepped on a trap...
# Hazelnuts collected: 0
#
# Test3:
# The squirrel is out of the field.
# Hazelnuts collected: 0
