# You are visiting Santa Claus' workshop, and it is complete chaos.
# You will need to help Santa find all items scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}".
# It is the Santa's workshop represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "Y"
# •	Christmas decorations are marked with the symbol "D"
# •	Gifts are marked with the symbol "G"
# •	Cookies are marked with the symbol "C"
# •	All empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End".
# The commands will be in the format "right/left/up/down-{steps}". You should move in the given direction with the given
# steps and collect all the items that come across. If you go out of the field, you should continue to traverse the
# field from the opposite side in the same direction. You should mark your path with "x".
# Your current position should always be marked with "Y".
# Keep track of all collected items.
# If you've collected all items at any point, end the program and print: "Merry Christmas!".
# Input
# •	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# •	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# •	On the following lines, you will receive commands in the format described above until
# you receive the command "End" or until you collect all items.
# Output
# •	On the first line, if you have collected all items, print:
# o	"Merry Christmas!"
# o	Otherwise, skip the line
# •	Next, print the number of collected items in the format:
# o	"You've collected:
# o	- {number_of_decoration} Christmas decorations
# o	- {number_of_gifts} Gifts
# o	- {number_of_cookies} Cookies"
# •	Finally, print the field, as shown in the examples.
# Constrains
# •	All the commands will be valid
# •	There will always be at least one item
# •	The dimensions of the matrix will be integers in the range [1, 20]
# •	The field will always have only one "Y"
# •	On the field, there will always be only the symbols shown above.
def is_in_range(r, c, r_size, c_size):
    return 0 <= r < r_size and 0 <= c < c_size


rows, cols = (int(x) for x in input().split(', '))
my_position = []
christmas_items = 0
christmas_decoration = 0
gifts = 0
cookies = 0


board = []
for r in range(rows):
    board.append(input().split(' '))
    for c in range(cols):
        if board[r][c] == 'Y':
            my_position = [r, c]
            board[r][c] = 'x'
        if board[r][c] in 'D, G, C':
            christmas_items += 1

possible_directions = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

while christmas_items > 0:
    command = input()

    if command == 'End':
        break

    position = command.split('-')[0]
    steps = int(command.split('-')[1])
    for direction in possible_directions:
        if direction == position:
            for i in range(1, steps+1):
                current_row = my_position[0] + possible_directions[direction][0]
                current_col = my_position[1] + possible_directions[direction][1]
                if not is_in_range(current_row, current_col, rows, cols):
                    current_row = my_position[0] - (possible_directions[direction][0] * (rows - 1))
                    current_col = my_position[1] - (possible_directions[direction][1] * (cols - 1))

                if board[current_row][current_col] == 'D':
                    christmas_decoration += 1
                    christmas_items -= 1
                elif board[current_row][current_col] == 'G':
                    gifts += 1
                    christmas_items -= 1
                elif board[current_row][current_col] == 'C':
                    cookies += 1
                    christmas_items -= 1
                board[my_position[0]][my_position[1]] = 'x'
                my_position = [current_row, current_col]
                board[my_position[0]][my_position[1]] = 'Y'

                if christmas_items == 0:
                    break

            break

if christmas_items == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {christmas_decoration} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(*el, sep=' ') for el in board]

# --- Tests: ---
# Test1:
# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End
#
# Test2:
# 5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3
#
# Test3:
# 5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End

# --- Outputs: ---
# Test1:
# You've collected:
# - 2 Christmas decorations
# - 1 Gifts
# - 0 Cookies
# . . . . .
# C . . G .
# . C . . .
# G . Y C .
# x x x x x
# x . x x x
#
# Test2:
# Merry Christmas!
# You've collected:
# - 2 Christmas decorations
# - 0 Gifts
# - 3 Cookies
# . . . . . .
# . . . . . .
# x x x x . .
# . . . x . .
# . . . Y . .
#
# Test3:
# You've collected:
# - 0 Christmas decorations
# - 0 Gifts
# - 0 Cookies
# x .
# Y x
# x x
# x .
# x G
