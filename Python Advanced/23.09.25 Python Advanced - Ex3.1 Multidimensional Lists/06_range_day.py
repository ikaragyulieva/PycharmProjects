# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated
# by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with the symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive.
# The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
# You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them -
# you can shoot only the nearest target. When you have shot a target, the field becomes an empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print:
# "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print:
# "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constraints
# •	All the commands will be valid
# •	There will always be at least one target

matrix = []
my_position = []
total_targets = 0
shoot_targets = []


for row in range(5):
    matrix.append(input().split())
    for column in range(5):
        if matrix[row][column] == 'A':
            my_position = [row, column]
        elif matrix[row][column] == 'x':
            total_targets += 1

possible_directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':

        if command[1] == 'up':
            r = my_position[0] - int(command[2])
            c = my_position[1]
        elif command[1] == 'down':
            r = my_position[0] + int(command[2])
            c = my_position[1]
        elif command[1] == 'left':
            r = my_position[0]
            c = my_position[1] - int(command[2])
        elif command[1] == 'right':
            r = my_position[0]
            c = my_position[1] + int(command[2])
        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [r, c]

    elif command[0] == 'shoot':
        direction = possible_directions[command[1]]
        shooting_row = my_position[0] + direction[0]
        shooting_column = my_position[1] + direction[1]
        while 0 <= shooting_row < 5 and 0 <= shooting_column < 5:
            if matrix[shooting_row][shooting_column] == 'x':
                matrix[shooting_row][shooting_column] = '.'
                shoot_targets.append([shooting_row, shooting_column])
                total_targets -= 1
                break
            shooting_row += direction[0]
            shooting_column += direction[1]
        if total_targets == 0:
            print(f"Training completed! All {len(shoot_targets)} targets hit.")
            break

if total_targets > 0:
    print(f"Training not completed! {total_targets} targets left.")

[print(x) for x in shoot_targets]
