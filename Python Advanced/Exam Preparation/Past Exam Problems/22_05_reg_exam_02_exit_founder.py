# Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out.
# Monitor their moves closely and find out who the winner will be!
# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ".
# The order in which they are received determines the order in which they will take turns. The first player starts first
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# •	Only one Exit - marked with the "E" letter
# •	Trap (one, many, or none) - marked with the "T" letter
# •	Wall (one, many, or none) - marked with the "W" letter
# •	Empty positions will be marked with "."
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given,
# you will be receiving coordinates for each of the players. They will be taking turns and stepping on different
# positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
# •	If a player hits the letter "E", he escapes the maze and wins the game.
# o	Print "{player} found the Exit and wins the game!" and end the program.
# •	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
# o	Print "{player} is out of the game! The winner is {winner}." and end the program.
# •	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
# o	Print "{player} hits a wall and needs to rest."
# •	If a player steps on an empty position ".", nothing happens.
# •	Both players can step in the same position at the same time.
# Input
# •	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
# •	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
# •	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
# Output
# •	You should print the output as described above.
# •	The input coordinates will always be valid.


name_player_1, name_player_2 = input().split(', ')
board_range = 6
board = [[c for c in input().split(' ')]for r in range(board_range)]

player_1_needs_rest = False
player_2_needs_rest = False
while True:
    command_player_1 = input().strip('()').split(', ')
    if not player_1_needs_rest:
        player_row, player_cow = (int(x) for x in command_player_1)
        if board[player_row][player_cow] == 'E':
            print(f"{name_player_1} found the Exit and wins the game!")
            break
        if board[player_row][player_cow] == 'T':
            print(f"{name_player_1} is out of the game! The winner is {name_player_2}.")
            break
        if board[player_row][player_cow] == 'W':
            print(f"{name_player_1} hits a wall and needs to rest.")
            player_1_needs_rest = True
    else:
        player_1_needs_rest = False

    command_player_2 = input().strip('()').split(', ')
    if not player_2_needs_rest:
        player_row, player_cow = (int(x) for x in command_player_2)
        if board[player_row][player_cow] == 'E':
            print(f"{name_player_2} found the Exit and wins the game!")
            break
        if board[player_row][player_cow] == 'T':
            print(f"{name_player_2} is out of the game! The winner is {name_player_1}.")
            break
        if board[player_row][player_cow] == 'W':
            print(f"{name_player_2} hits a wall and needs to rest.")
            player_2_needs_rest = True
    else:
        player_2_needs_rest = False

# --- Tests: ---
# Test1:
# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
#
# Test2:
# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)
#
# Test3:
# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
#
#
# --- Output: ---
# Test1:
# Tom hits a wall and needs to rest.
# Jerry is out of the game! The winner is Tom.
#
# Test2:
# Jerry found the Exit and wins the game!
#
# Test3:
# Jerry hits a wall and needs to rest.
# Tom hits a wall and needs to rest.
# Tom hits a wall and needs to rest.
# Jerry hits a wall and needs to rest.
# Tom found the Exit and wins the game!
