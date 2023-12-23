# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
# with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
# If the cell has an "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is
# marked with "V". There can also be cells marked with "C" for cookies.
# All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", and "right" with one position each time.
# These will be the commands that you receive. If he moves to a house with a nice kid, the kid receives a present,
# but if Santa reaches a house with a naughty kid, he doesn't drop a present.
# If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all
# the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice).
# If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to
# these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# •	On the first line, you are given the integer m - the count of presents
# •	On the second - integer n - the size of the neighborhood
# •	The following n lines hold the values for every row
# •	On each of the following lines you will get a command
# Output
# •	On the first line:
# o	If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# •	Next, print the matrix.
# •	In the end, print one of these messages:
# o	If he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# o	Otherwise, print:
# "No presents for {count nice kids} nice kid/s."
# Constraints
# •	The size of the square matrix will be between [2…10].
# •	Santa's position will be marked with an 'S'.
# •	There will always be at least 1 nice kid.
# •	There won't be a case where the cookie is on the border of the matrix.

presents = int(input())
neighborhood_size = int(input())
neighborhood = []
santa = []
nice_kids = 0
kids_with_presents = 0

for row in range(neighborhood_size):
    neighborhood.append([x for x in input().split()])
    for column in range(neighborhood_size):
        if neighborhood[row][column] == 'S':
            santa = [row, column]
        if neighborhood[row][column] == 'V':
            nice_kids += 1

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while True:
    command = input()

    if command == 'Christmas morning':
        break

    santa_row = santa[0] + directions[command][0]
    santa_column = santa[1] + directions[command][1]
    if 0 <= santa_row < neighborhood_size and 0 <= santa_column < neighborhood_size:
        if neighborhood[santa_row][santa_column] == 'V':
            presents -= 1
            kids_with_presents += 1
        elif neighborhood[santa_row][santa_column] == 'C':

            for direction in directions:
                if presents > 0:
                    if neighborhood[santa_row + directions[direction][0]][santa_column + directions[direction][1]] == 'V':
                        kids_with_presents += 1
                        presents -= 1
                    elif neighborhood[santa_row + directions[direction][0]][santa_column + directions[direction][1]] == 'X':
                        presents -= 1
                    neighborhood[santa_row + directions[direction][0]][santa_column + directions[direction][1]] = '-'

        neighborhood[santa[0]][santa[1]] = '-'
        neighborhood[santa_row][santa_column] = 'S'
        santa = [santa_row, santa_column]

    if nice_kids == kids_with_presents:
        break

    if presents <= 0 and nice_kids != kids_with_presents:
        print("Santa ran out of presents!")
        break

[print(*x) for x in neighborhood]
if kids_with_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - kids_with_presents} nice kid/s.")
