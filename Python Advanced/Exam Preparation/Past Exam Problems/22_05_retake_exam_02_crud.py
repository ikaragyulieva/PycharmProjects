# The abbreviation CRUD expands to Create, Read, Update and Delete.
# These are the four fundamental operations in a database.
#
# In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information.
# It consists of:
# •	Letters - on one or many positions in the table
# •	Numbers - on one or many positions in the table
# •	Empty positions - marked with "."
#
# Next, you will receive your first position on the table in the format "({row}, {column})"
# On the following lines, until you receive "Stop" you will be receiving commands in the format:
# •	"Create, {direction}, {value}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step in an empty position, create the given value on that position. E.g., if the given value is "A",
# and the position is empty (".") - change it to "A"
# o	If the position is NOT empty, do NOT create a value on that position
# •	"Update, {direction}, {value}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, update the position with the given value. E.g., if the given value is "h",
# and the position's value is "12" - change it to "h"
# o	If the position is empty, do NOT update the value on that position
# •	"Delete, {direction}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" -
# change it to "."
# o	If the position is already empty, do NOT delete it
# •	"Read, {direction}"
# o	The direction could be "up", "down", "left" or "right"
# o	If you step on a letter or number, print it on the console
# o	If the position is empty, do NOT read it
# You can make only ONE move at a time in the given direction for each command given.
# In the end, print the final matrix.
# Input
# •	On the first 6 lines - a matrix with positions separated by a single space
# o	Letters are in the range [a-zA-Z]
# o	Numbers are in the range [-100, 100]
# •	On the next line - your first position in the format: "({row}, {column})"
# •	On the following lines until you receive the command "Stop" - commands in the format shown above
# Output
# •	In the end, print the final matrix, each row on a new line, each position separated by a single space.
# Constraints
# •	You will always receive valid coordinates
# •	You will always receive directions in the range of the table
# •	You will always receive letters or numbers

n = 6
matrix = [[el for el in input().split(' ')]for _ in range(n)]
position_row, position_col = map(int, input().strip('()').split(', '))

possible_directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

while True:
    command_input = input()
    if command_input == 'Stop':
        break
    command = command_input.split(', ')
    action = command[0]
    direction = command[1]
    position_row += possible_directions[direction][0]
    position_col += possible_directions[direction][1]
    if action == 'Create':
        if matrix[position_row][position_col] == '.':
            matrix[position_row][position_col] = command[2]
    elif action == 'Update':
        if matrix[position_row][position_col] != '.':
            matrix[position_row][position_col] = command[2]
    elif action == 'Delete':
        if matrix[position_row][position_col] != '.':
            matrix[position_row][position_col] = '.'
    elif action == 'Read':
        if matrix[position_row][position_col] != '.':
            print(matrix[position_row][position_col])

[print(*el, sep=' ') for el in matrix]

# --- Tests: ---
# Test1:
# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop
#
# Test2:
# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
# (2, 3)
# Create, down, o
# Delete, right
# Read, up
# Create, left, 20
# Update, up, P
# Stop
#
# Test3:
# H 8 . . . .
# 70 i . . . .
# t . . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
# (0, 0)
# Read, right
# Read, down
# Read, left
# Delete, down
# Create, right, 10
# Read, left
# Stop
#
# --- Outputs: ---
# Test1:
# t
# . . . . . .
# . 6 . . . .
# G r e a t .
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
#
# Test2:
# . . . . . .
# . 6 . . . .
# . T . D . O
# . . 10 A . .
# . 95 . 80 5 .
# . . P . t .
#
# Test3:
# 8
# i
# 70
# H 8 . . . .
# 70 i . . . .
# . 10 . . B .
# 50 . 16 . C .
# . . . t . .
# . 25 . . . .
