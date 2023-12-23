# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape.
# On the following n lines, you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A".
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position,
# she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
# and she does not need to continue collecting. Otherwise, if she steps into the rabbit hole or goes out of the
# territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command
# Output
# •	On the first line:
# o	If Alice steps into the rabbit hole or goes out of the territory, print:
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# •	On the following lines, print the matrix.
# Constraints
# •	Alice will always either go outside Wonderland or collect 10 bags of tea
# •	All the commands will be valid
# •	All of the given numbers will be valid integers in the range [0, 10]

n = int(input())

matrix = []
alice = []

for i in range(n):
    matrix.append([x for x in input().split(' ')])
    for j in range(n):
        if matrix[i][j] == 'A':
            matrix[i][j] = '*'
            alice = [i, j]


tea_bags = 0

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while tea_bags < 10:
    command = input()
    move = possible_moves[command]
    alice[0] += move[0]
    alice[1] += move[1]

    if alice[0] < 0 or alice[0] >= n or alice[1] < 0 or alice[1] >= n:
        break
    if matrix[alice[0]][alice[1]] == 'R':
        matrix[alice[0]][alice[1]] = '*'
        break
    if matrix[alice[0]][alice[1]] not in '*.':
        tea_bags += int(matrix[alice[0]][alice[1]])
    matrix[alice[0]][alice[1]] = '*'


if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")
[print(*r) for r in matrix]
