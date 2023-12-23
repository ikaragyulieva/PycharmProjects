# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space.
# The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line.
# The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively,
# moving with only one position in the given direction. If the miner has reached the edge of the field and
# the following command indicates that he has to get out of the area,
# he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*".
# Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting
# the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message:
# "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message:
# "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message:
# "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# •	There are three types of output as mentioned above.
# Constraints
# •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# •	The field will always have only one "s"
def are_in_range(command_row, command_column, matrix_range):
    return 0 <= command_row < matrix_range and 0 <= command_column < matrix_range


n = int(input())
commands = input().split(' ')
matrix = []

current_row, current_col = 0, 0
coals_num = 0
game_over = False

for row in range(n):
    matrix.append(input().split(' '))
    for col in range(n):
        if matrix[row][col] == 's':
            current_row, current_col = row, col
        elif matrix[row][col] == 'c':
            coals_num += 1

for command in commands:
    if command == 'up':
        if are_in_range(current_row-1, current_col, n):
            current_row -= 1
    elif command == 'down':
        if are_in_range(current_row+1, current_col, n):
            current_row += 1
    elif command == 'left':
        if are_in_range(current_row, current_col-1, n):
            current_col -= 1
    elif command == 'right':
        if are_in_range(current_row, current_col+1, n):
            current_col += 1

    if matrix[current_row][current_col] == 'e':
        print(f"Game over! ({current_row}, {current_col})")
        game_over = True
        break
    elif matrix[current_row][current_col] == 'c':
        coals_num -= 1
        matrix[current_row][current_col] = '*'

        if coals_num == 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            game_over = True
            break

if not game_over:
    print(f"{coals_num} pieces of coal left. ({current_row}, {current_col})")
