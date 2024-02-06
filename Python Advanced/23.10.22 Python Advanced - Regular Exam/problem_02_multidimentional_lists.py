# You are a longtime captain of an old fishing vessel.
# The new fishing season begins and you prepare your ship to set sail in search of the big catch…
# You will be given an integer n for the size of the fishing area with a square shape.
# On the next n lines, you will receive the rows of the fishing area. You will be placed in a random position, marked
# with the letter 'S'. There will be fishing passages on random positions, marked with a single digit.
# There will be whirlpools marked with 'W'. All empty positions will be marked with '-'.
# Each turn until the "collect the nets" command is received you will be given commands for your movement.
# Move commands will be: "up", "down", "left", and "right".
# •	If you move to a fish passage, you collect the amount equal to the digit there,
# the passage disappears and should be replaced by '-'.
# •	If you fall into a whirlpool – the ship sinks and loses its catch, the program ends.
# •	If you leave the fishing area (go out of the boundaries of the matrix)
# depending on the move command you will be moved to the opposite side of the one you were on.
# /Example: In a 3x3 matrix you are at position [1,2] and receive the command "right"
# you will be moved to position [1,0]./
#  You need at least 20 tons of fish to be considered a successful season.
#  Keep in mind that even if the quota is reached the ship continues to move.
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines hold the values for every row.
# •	On each of the next lines, you will get a move command.
# Output
# •	On the first line:
# 	If the ship falls into a whirlpool, print only this message and stop the program:
# o	"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [n,n]"
# 	If the ship reaches the quota:
# o	"Success! You managed to reach the quota!"
# 	If the ship did not reach the quota:
# o	"You didn't catch enough fish and didn't reach the quota!
# You need {lack of fish} tons of fish more."
# •	On the next lines.
# 	If the catch quantity is bigger than zero, print:
# o	"Amount of fish caught: {quantity} tons."
# else: do not print anything.
# 	If you didn't get into a whirlpool, print the matrix.
# Constraints
# •	The size of the square matrix will be between [2…10].
# •	Only the letters 'S' and 'W' will be present in the matrix.
# •	The fish passages are represented by single positive digits /tons/ between [1…9].
# •	It is expected that there will only be either zero or one whirlpool present, marked with the letter - 'W'.
# •	Your position will be marked with 'S'.

def is_in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


def ship_movement(player, current_command, movement_directions, board):
    move_row = 0
    move_col = 0
    for direction, moves in movement_directions.items():
        if current_command == direction:
            move_row = player[0] + moves[0]
            move_col = player[1] + moves[1]
            if not is_in_range(move_row, move_col, board):
                move_row = player[0] - (moves[0] * (board - 1))
                move_col = player[1] - (moves[1] * (board - 1))
                break

    return move_row, move_col


n = int(input())
ship_position = []
fishing_area = []
collected_fish = 0
game_over = False
for r in range(n):
    item = list(input())
    fishing_area.append(item)
    for c in range(n):
        if fishing_area[r][c] == 'S':
            ship_position = r, c

possible_directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while not game_over:
    command = input()
    if command == 'collect the nets':
        break
    new_row, new_col = ship_movement(ship_position, command, possible_directions, n)
    if fishing_area[new_row][new_col] == 'W':
        ship_position = new_row, new_col
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{new_row},{new_col}]")
        game_over = True
        break
    if fishing_area[new_row][new_col] == '-':
        fishing_area[ship_position[0]][ship_position[1]] = '-'
        ship_position = new_row, new_col
        fishing_area[ship_position[0]][ship_position[1]] = 'S'
        continue

    collected_fish += int(fishing_area[new_row][new_col])

    fishing_area[ship_position[0]][ship_position[1]] = '-'
    ship_position = new_row, new_col
    fishing_area[ship_position[0]][ship_position[1]] = 'S'

if not game_over:
    if collected_fish >= 20:
        print("Success! You managed to reach the quota!")
    elif collected_fish < 20:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")
    if collected_fish > 0:
        print(f"Amount of fish caught: {collected_fish} tons.")

    [print(*r, sep='') for r in fishing_area]

# --- Tests: ---
# Test1:
# 4
# ---S
# ----
# 9-5-
# 34--
# down
# down
# right
# down
# collect the nets
#
# Test2:
# 5
# S---9
# 777-1
# W333-
# 11111
# -----
# down
# down
# right
# down
# collect the nets
#
# Test3:
# 5
# S---9
# 777-1
# --5--
# 11W11
# 988--
# down
# down
# down
# down
# down
# down
# right
# right
# right
# collect the nets

# --- Outputs: ---
# Test1:
# You didn't catch enough fish and didn't reach the quota! You need 8 tons of fish more.
# Amount of fish caught: 12 tons.
# ----
# ----
# --5-
# S4--
#
# Test2:
# You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [2,0]
# Test3:
# Success! You managed to reach the quota!
# Amount of fish caught: 31 tons.
# ----9
# ---S1
# --5--
# -1W11
# -88--
