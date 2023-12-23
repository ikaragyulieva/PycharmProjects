# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1")
# and ("row2", "col2") are the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
# separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
# (thus, you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
# or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
# A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

def are_in_range(r1, c1, r2, c2, r, c):
     return 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c2 < c

rows, columns = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for r in range(rows)]

while True:

    command = input()
    if command == 'END':
        break

    # command = command_input[0]
    # row_one = int(command_input[1])
    # col_one = int(command_input[2])
    # row_two = int(command_input[3])
    # col_two = int(command_input[4])
    command_input = command.split()
    if len(command_input) != 5 or command_input[0] != 'swap':
        print("Invalid input!")
        continue

    row_one, col_one, row_two, col_two = [int(x) for x in command_input[1:]]

    if are_in_range(row_one, col_one, row_two, col_two, rows, columns):
        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
