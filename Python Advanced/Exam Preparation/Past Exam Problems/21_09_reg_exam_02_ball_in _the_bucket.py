# You are at the fun fair to play different games and test your skills. Now you are playing ball in the bucket game.
# You will be given a matrix with 6 rows and 6 columns representing the board. On the board,
# there will be points (integers) and buckets marked with the letter "B". Rules of the game:
# •	You can throw a ball only 3 times.
# •	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
# •	You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
# •	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
# After the board state, you are going to receive the information for every throw on a separate line.
# The coordinates’ information of a hit will be in the format: "({row}, {column})".
# Depending on how many points you have collected, you win one of the following:
# Football	100 to 199 points
# Teddy Bear	200 to 299 points
# Lego Construction Set	300 and more points
#
# Your job is to keep track of the scored points and to check if you won a prize.
# For more clarifications, see the examples below.
# Input
# •	6 lines – matrix representing the board (each position separated by a single space)
# •	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"
#
# Output
# •	On the first line:
# o	If you won a prize, print:
# "Good job! You scored {points} points, and you've won {prize}."
# o	If you did not win any prize, print the points you need to get at least the first prize:
# "Sorry! You need {points} points more to win a prize."
# Constraints
# •	All the given points will be integers in the range [1, 30]
# •	All the given indexes will be integers in the range [0, 30]
# •	There always will be exactly 6 buckets - 1 on each column

def is_in_range(r, c, size):
    return 0 <= r < size and 0 <= c < size


def shoot(row, col, matrix):
    score_count = 0
    for i in range(1, 6):
        current_row = row + i
        if is_in_range(current_row, col, board_range):
            score_count += int(matrix[current_row][col])
        else:
            break
    for i in range(1, 6):
        current_row = row - i
        if is_in_range(current_row, col, board_range):
            score_count += int(matrix[current_row][col])
        else:
            break
    return score_count


def wins(collected_score):
    prize = ''
    if 100 <= collected_score < 200:
        prize = 'Football'
    if 200 <= collected_score < 300:
        prize = 'Teddy Bear'
    if collected_score >= 300:
        prize = 'Lego Construction Set'
    return prize


board_range = 6
board = [[el for el in input().split()]for x in range(6)]
hit_buckets = []
score = 0

for intent in range(3):
    shooting_row, shooting_column = (int(x) for x in input().strip('()').split(', '))
    if not is_in_range(shooting_row, shooting_column, board_range) or [shooting_row, shooting_column] in hit_buckets:
        continue

    if board[shooting_row][shooting_column] == 'B':
        hit_buckets.append([shooting_row, shooting_column])
        score += shoot(shooting_row, shooting_column, board)


if score >= 100:
    print(f"Good job! You scored {score} points, and you've won {wins(score)}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")


# --- Tests ---
# Test1:
# 10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)
#
# Test:2
# B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)

# --- Outputs ---
# Test1: Sorry! You need 33 points more to win a prize.
# Test2: Good job! You scored 299 points, and you've won Teddy Bear.
