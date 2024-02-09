# Write function called best_list_pureness which will receive a list of numbers and a number K.
# You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness
# (pureness is calculated by summing all the elements in the list multiplied by their indices).
# For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
# At the end the function should return a string containing the highest pureness and the amount of rotations that were
# made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations"
# If there is more than one highest pureness, take the first one.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	There is no expected output
# •	The function should return a string in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations"

# https://judge.softuni.org/Contests/2551/Python-Advanced-Exam-24-October-2020

from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    rotations = min(args[1], len(numbers))
    best_pureness = float('-inf')
    best_pureness_rotation = 0
    for rotation in range(rotations + 1):
        pureness = 0
        for index, num in enumerate(numbers):
            pureness += index * num
        if pureness > best_pureness:
            best_pureness = pureness
            best_pureness_rotation = rotation
        numbers.rotate()

    return f"Best pureness {best_pureness} after {best_pureness_rotation} rotations"


# --- Tests: ---


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
