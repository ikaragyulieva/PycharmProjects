# Write a program that reads a matrix from the console and changes its values.
# On the first line, you will get the matrix's rows - N.
# You will get elements for each column on the following N lines, separated with a single space.
# You will be receiving commands in the following format:
# •	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# •	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in the range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

def valid_coordinates(row, col, row_range, col_range):
    return 0 <= row < row_range and 0 <= col < col_range


n = int(input())

matrix = [[int(i) for i in input().split(' ')]for _ in range(n)]
print(matrix)
while True:

    command = input().split(' ')

    if command[0] == 'END':
        [print(*r, sep=' ', end='\n') for r in matrix]
        break

    row = int(command[1])
    column = int(command[2])
    value = int(command[3])

    if valid_coordinates(row, column, n, len(matrix[1])):
        if command[0] == 'Add':
            matrix[row][column] += value
        elif command[0] == 'Subtract':
            matrix[row][column] -= value
    else:
        print("Invalid coordinates")

