# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
# •	One rover - marked with the letter "E"
# •	Water deposit (one or many) - marked with the letter "W"
# •	Metal deposit (one or many) - marked with the letter "M"
# •	Concrete deposit (one or many) - marked with the letter "C"
# •	Rock (one or many) - marked with the letter "R"
# •	Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement on one line separated by a comma and a
# space (", "). Commands can be: "up", "down", "left", or "right".
# For each command, the rover moves in the given directions with one step,
# and it can land on one of the given types of deposit or a rock:
# •	When it lands on a deposit, you must print the coordinates of that deposit in the format
# shown below and increase its value by 1.
# •	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below,
# and the program ends.
# •	If the rover goes out of the field, it should continue from the opposite side in the same direction.
# Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix),
# it should be placed at position (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
# Stop the program if you run out of commands or the rover gets broken.
# Input
# •	On the first 6 lines, you will receive the matrix.
# •	On the following line, you will receive the commands for the rover separated by a comma and a space.
# Output
# •	For each deposit found while you go through the commands, print out on the console:
# "{Water, Metal or Concrete} deposit found at ({row}, {col})"
# •	If the rover hits a rock, print the coordinates where it got broken in the format:
# "Rover got broken at ({row}, {col})"
# After you go through all the commands or the rover gets broken, print out on the console:
# •	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
# •	Otherwise, print on the console: "Area not suitable to start the colony."
# See examples for more clarification.

def is_in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


def rover_movement(rover, current_command, movement_directions, size):
    move_row = 0
    move_col = 0
    for direction, moves in movement_directions.items():
        if current_command == direction:
            move_row = rover[0] + moves[0]
            move_col = rover[1] + moves[1]
            if not is_in_range(move_row, move_col, board_range):
                move_row = rover[0] - (moves[0] * (size - 1))
                move_col = rover[1] - (moves[1] * (size - 1))
    return move_row, move_col


board_range = 6
board = []
rover_position = []
metal = False
water = False
concrete = False

for r in range(6):
    board.append(input().split(' '))
    for c in range(6):
        if board[r][c] == 'E':
            rover_position = [r, c]

commands = [x for x in input(). split(', ')]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
for command in commands:

    new_row, new_col = rover_movement(rover_position, command, directions, board_range)
    if board[new_row][new_col] == 'W':
        water = True
        print(f"Water deposit found at ({new_row}, {new_col})")
    elif board[new_row][new_col] == 'M':
        print(f"Metal deposit found at ({new_row}, {new_col})")
        metal = True
    elif board[new_row][new_col] == 'C':
        print(f"Concrete deposit found at ({new_row}, {new_col})")
        concrete = True
    elif board[new_row][new_col] == 'R':
        print(f"Rover got broken at ({new_row}, {new_col})")
        break
    rover_position = [new_row, new_col]

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



# --- Tests: ---
# Test1:
# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left
#
# Test2:
# R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right
#
# Test3:
# R - - - - -
# - - C - - -
# - - - - M -
# C - M - R M
# - E - W - -
# - - - - - -
# right, right, up, left, left, left, left, left
#
#
# --- Outputs: ---
# Test1:
# Water deposit found at (3, 1)
# Concrete deposit found at (4, 3)
# Metal deposit found at (5, 0)
# Area suitable to start the colony.
#
# Test2:
# Water deposit found at (3, 2)
# Water deposit found at (4, 3)
# Rover got broken at (4, 5)
# Area not suitable to start the colony.
#
# Test3:
# Water deposit found at (4, 3)
# Metal deposit found at (3, 2)
# Concrete deposit found at (3, 0)
# Metal deposit found at (3, 5)
# Rover got broken at (3, 4)
# Area suitable to start the colony.
