# It's time for one of the biggest races in the world, Paris-Dakar. The organizers of the event want you to do a program
# that helps them track the cars through the separate stages in the event.
#
# On the first line, you will be given an integer N, which represents the size of a square matrix.
# On the second line you will receive the racing number of the tracked race car.
# On the next N lines you will be given the rows of  the matrix (string sequences, separated by whitespace),
# which will be representing the race route. The tracked race car always starts with coordinates [0, 0].
# There will be a tunnel somewhere across the race route. If the race car runs into the tunnel , the car goes through it
# and exits at the other end. There will be always two positions marked with "T"(tunnel). The finish line will be marked
# with "F". All other positions will be marked with ".".
# Keep track of the kilometers passed. Every time the race car receives a direction and moves to the next position of
# the race route, it covers 10 kilometers. If the car goes through the tunnel, it covers NOT 10, but 30 kilometers.
# On each line, after the matrix is given, you will be receiving the directions for the race car.
# •	left
# •	right
# •	up
# •	down
# The race car starts moving across the race route:
# •	If you receive "End" command, before the race car manages to reach the finish line, the car is disqualified and the
# following output should be printed on the Console: "Racing car {racing number} DNF."
# •	If the race car comes across a position marked with ".".
# The car passes 10 kilometers for the current move and waits for the next direction.
# •	If the race car comes across a position marked with "T" this is the tunnel.
# The race car goes through it and moves to the other position marked with  "T" (the other end of the tunnel).
# The car passes 30 kilometers for the current move. The tunnel stays behind the car, so the race route is clear,
# and both the positions marked with "T", should be marked with ".".
# •	If the car reaches the finish line - "F" position, the race is over.
# The tracked race car manages to finish the stage and the following output should be printed on the Console: "Racing
# car {racing number} finished the stage!". Don’t forget that the car has covered another 10 km with the last move.
# Input
# •	On the first line you will receive N - the size of the square matrix (race route)
# •	On the second line you will receive the racing number of the tracked car
# •	On the next N lines, you will receive the race route (elements will be separated by a space).
# •	On the following lines, you will receive directions (left, right, up, down).
# •	On the last line, you will receive the command "End".
# Output
# •	If the racing car has reached the finish line before the "End" command is given, print on the Console:
# "Racing car {racing number} finished the stage!"
# •	If the "End"  command is given and the racing car has not reached the finish line yet, the race ends and the
# following message is printed on the Console: "Racing car {racing number} DNF."
# •	On the second line, print the distance that the tracked race car has covered:
# "Distance covered {kilometers passed} km."
# •	At the end, mark the last known position of the race car with "C" and print the final state of
# the matrix (race route). The row elements in the output matrix should NOT be separated by a whitespace.
# Constraints
# •	The directions will always lead to coordinates in the matrix.
# •	There will always be two positions marked with "T" , representing the tunnel in the race route.
# •	The size of the square matrix (race route) will be between [4…10].

# def is_in_range(c, board):
#     return 0 <= c < board


def car_movement(car, current_command, movement_directions):
    move_row = 0
    move_col = 0
    for direction, moves in movement_directions.items():
        if current_command == direction:
            move_row = car[0] + moves[0]
            move_col = car[1] + moves[1]
            break
    return move_row, move_col


# def tunel_passing(row, col, matrix, board_size):
#     out_row = 0
#     out_col = 0
#     while matrix[row][col] != 'T':
#         out_row = row
#         out_col = col + 1
#         if not is_in_range(out_col, board_size):
#             out_row += 1
#             out_col -= board_size
#         elif not is_in_range(out_row, board_size):
#             out_row -= board_size
#         if matrix[out_row][out_col] == 'T':
#             break
#         row = out_row
#         col = out_col
#     return out_row, out_col


def find_end_of_dune(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == "T":
                return row, col


n = int(input())
car_number = input()
car_position = (0, 0)
route = [input().split(' ') for r in range(n)]
distance_passed = 0
possible_directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()
    if command == 'End':
        route[car_position[0]][car_position[1]] = 'C'
        print(f"Racing car {car_number} DNF.")
        break
    current_row, current_col = car_movement(car_position, command, possible_directions)
    route[car_position[0]][car_position[1]] = '.'
    if route[current_row][current_col] == '.':
        distance_passed += 10
    elif route[current_row][current_col] == 'F':
        distance_passed += 10
        route[current_row][current_col] = 'C'
        print(f"Racing car {car_number} finished the stage!")
        break
    elif route[current_row][current_col] == 'T':
        route[current_row][current_col] = '.'
        distance_passed += 30
        # current_row, current_col = tunel_passing(current_row, current_col, route, n)
        current_row, current_col = find_end_of_dune(route)
    car_position = current_row, current_col
    route[car_position[0]][car_position[1]] = 'C'

print(f"Distance covered {distance_passed} km.")
[print(*r, sep='') for r in route]

# --- Tests: ---
# Test1:
# 5
# 01
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .
# down
# right
# right
# right
# down
# right
# up
# down
# right
# up
# End
#
# Test2:
# 10
# 45
# . . . . . . . . . .
# . . T . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . F . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . T . .
# right
# down
# down
# right
# up
# left
# up
# up
# End
#
# --- Outputs: ---
# Test1:
# Racing car 01 finished the stage!
# Distance covered 80 km.
# .....
# .....
# .....
# .....
# ..C..
#
# Test2:
# Racing car 45 DNF.
# Distance covered 100 km.
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ......F...
# ......C...
# ..........
# ..........
