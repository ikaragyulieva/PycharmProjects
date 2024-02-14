# "It's only when you are flying above that you realize how incredible the Earth really is."
# As you know, stewards are needed for every single flight. Today you will be that one steward,
# and you will be assisting the passengers in finding their seats.
# You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format
# "{number}{letter}". You will also be given two more sequences of numbers only.
# First, you have to take the first number of the first sequence and the last number of the second sequence.
# Next, take the sum of those two numbers and find its ASCII character.
# •	Compare each of the two taken numbers and the found character with the seats. If you find a match,
# the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
# •	If there is no equality, the two numbers should be returned at the end of their sequences
# (first becomes last, last becomes first).
# •	If you match an already taken seat, you should just remove both numbers from their sequences.
# Each time you take numbers from the sequences and try to match them, you make one rotation.
# You should keep track of all rotations made.
# The program should end under the following circumstances:
# •	You have found 3 (three) seat matches
# •	You have made a total of 10 rotations
# Input
# •	On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
# •	On the second and the third line, you will be given two more sequences -
# integers separated by a comma and a space ", "
# Output
# When the program ends, print the following on two different lines:
# o	Seat matches: {matches separated by comma and space}
# o	Rotations count: {total rotations made}
# Constraints
# •	All integers will be in the range [1, 100]
# •	All letters will be in the range [A-Z]
# •	You will never run out of numbers in your sequences before the program ends
# •	You will never have more than one match at a time

from collections import deque

seats = input().split(', ')
seq_1 = deque(int(el) for el in input().split(', '))
seq_2 = deque(int(el) for el in input().split(', '))

rotations = 0
seat_matches = []

while rotations < 10 and len(seat_matches) < 3:
    rotations += 1
    current_seq_1 = seq_1[0]
    current_seq_2 = seq_2[-1]
    character = chr(current_seq_1 + current_seq_2)
    seat_option1 = str(current_seq_1)+character
    seat_option2 = str(current_seq_2)+character
    if seat_option1 not in seats and seat_option2 not in seats:
        seq_1.rotate(-1)
        seq_2.insert(0, seq_2.pop())
        continue

    for seat in seats:
        if seat_option1 == seat or seat_option2 == seat and seat not in seat_matches:
            seq_1.popleft()
            seq_2.pop()
            seats.remove(seat)
            seat_matches.append(seat)
            break


print(f"Seat matches: {', '.join(str(x) for x in seat_matches)}")
print(f"Rotations count: {rotations}")

# --- Tests: ---
# Test1:
# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46
#
# Test2:
# 25A, 16B, 44T, 49D, 27M, 44F
# 25, 3, 31, 49, 26, 13
# 10, 15, 44, 40
#
# Test3:
# 15C, 25C, 36C, 43P, 40E, 38G
# 15, 25, 80, 40, 15, 99, 52
# 15, 42, 29
#
#
# --- Outputs: ---
# Test1:
# Seat matches: 20B, 15D, 3C
# Rotations count: 4
#
# Test2:
# Seat matches: 25A, 44F
# Rotations count: 10
#
# Test3:
# Seat matches: 25C, 40E, 15C
# Rotations count: 7
