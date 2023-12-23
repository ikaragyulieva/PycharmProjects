# Chess is the oldest game, but it is still popular these days.
# You will use only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column, or diagonal.
# (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally
# then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with a "K" for knights and a "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.
# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"
# Output
# •	Print a single integer with the number of knights that need to be removed.
# Constraints
# •	The size of the board will be 0 < N < 30
# •	Time limit: 0.3 sec. Memory limit: 16 MB

n = int(input())

matrix = []
knights = []

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0

while True:
    max_hits = 0
    max_hits_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in moves:
            new_row = k_row + move[0]
            new_column = k_col + move[1]
            if 0 <= new_row < n and 0<= new_column < n:
                if matrix[new_row][new_column] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_hits_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_hits_knight)
    matrix[max_hits_knight[0]][max_hits_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)


