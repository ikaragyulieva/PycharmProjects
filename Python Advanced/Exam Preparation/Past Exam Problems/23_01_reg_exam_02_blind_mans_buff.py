# Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player,
# is blindfolded and gropes around attempting to touch the other players without being able to see them…
# You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive
# the rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random position.
# In random positions, furniture or other obstacles will be marked with the letter 'O'. The other players (opponents)
# will be marked with the letter 'P'. There will always be three other players participating in the game.
# All of the empty positions will be marked with '-'.
# Your goal is to touch as many players as possible during the game,
# without leaving the playground or stepping on an obstacle.
# On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing
# which direction you need to move. The possible directions are "up", " down", "right", and "left". If the direction
# leads you out of the field, you need to stay in position inside the field(do NOT make the move).
# If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.
# You need to keep track of the count of touched opponents and the moves you’ve made.
# In case you step on a position marked with '-', increase the count of the moves made.
# When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
# If there is an opponent, you touch him and the position is marked with '-'
# increase the count of the touched opponents and moves made), and this is your new position.
# The game is over when you manage to touch all other opponents or the given command is "Finish".
# A game report is printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"
#
# Input
# •	On the first line, you'll receive the dimensions of the playground in the format: "N M", where N is the number of
# rows, and M is the number of columns. They'll be separated by a single space (" ").
# •	On the next N lines, you will receive a string representing the respective row of the playground.
# The positions in every string will be separated by a single space (" ").
# •	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).
#  
# Output
# •	When the game is over, the following output should be printed on the Console:
# "Game over!"
# "Touched opponents: {count} Moves made: {count}"
# Constraints
# •	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
# •	The playground will always have three opponents in it - 'P'.
# •	The obstacles on the playground will always be random count, and there will be cases without any obstacles.


def is_in_range(r, c, board_r, board_c):
    return 0 <= r < board_r and 0 <= c < board_c


def player_movement(player, current_command, movement_directions):
    move_row = 0
    move_col = 0
    for direction, moves in movement_directions.items():
        if current_command == direction:
            move_row = player[0] + moves[0]
            move_col = player[1] + moves[1]
            break
    return move_row, move_col


rows, columns = (int(x) for x in input().split(' '))
blind_position = []
playground = []
players = 0
moves = 0
for r in range(rows):
    playground.append(input().split(' '))
    for c in range(columns):
        if playground[r][c] == 'B':
            blind_position = r, c


possible_directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while players < 3:
    command = input()
    if command == 'Finish':
        break
    moves += 1
    move_row, move_col = player_movement(blind_position, command, possible_directions)
    if not is_in_range(move_row, move_col, rows, columns):
        moves -= 1
        continue
    if playground[move_row][move_col] == 'O':
        moves -= 1
        continue
    if playground[move_row][move_col] == 'P':
        players += 1
        playground[move_row][move_col] = '-'

    blind_position = move_row, move_col

print("Game over!")
print(f"Touched opponents: {players} Moves made: {moves}")

# --- Tests: ---
# Test1:
# 5 8
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -
# up
# up
# left
# Finish
#
# Test2:
# 4 4
# O B O -
# - P O P
# - - P -
# - - - -
# left
# right
# down
# right
# down
# right
# up
# right
# up
# down
# Finish
#
# --- Outputs: ---
# Test1:
# Game over!
# Touched opponents: 1 Moves made: 3
#
# Test2:
# Game over!
# Touched opponents: 3 Moves made: 5
