# Rubber Duck Debugging is a type of debugging where you place a rubber duck on your desk and explain to it your code
# line by line. You gathered a few programmers and gave them a task and judging by the time it took them to write the
# code, you reward them with a type of rubber ducky.
# Learn more about Rubber Duck Debugging after your exam from here.
# You will be given two sequences of integers. The first one represents the time it takes a programmer to complete a
# single task. The second one represents the number of tasks you’ve given to your programmers.
# Your task is to count how many rubber ducks of each type you’ve given to your programmers.
# While you have values in the sequences, you need to start from the first value of the programmers time's sequence and
# multiply them by the last value of the tasks' sequence:
# •	If the calculated time is between any of the time ranges below, you give the corresponding ducky and remove the
# programmer time's value and the tasks' value.
# •	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2.
# Then, move the programmer time's value to the end of its sequence, and continue with the next operation
# Rubber Ducky type	Time needed to earn it
# Darth Vader Ducky	0 - 60
# Thor Ducky	61 – 120
# Big Blue Rubber Ducky	121 - 180
# Small Yellow Rubber Ducky	181 - 240
# Your task is considered done when the sequences are empty.
# Input
# •	The first line will represent each programmer’s time to complete a single task – integers,
# separated by a single space.
# •	The second line will represent the number of tasks that should be completed – integers, separated by a single space.
# Output
# •	On the first line, you output:
# o	"Congratulations, all tasks have been completed! Rubber ducks rewarded:"
# •	On the next 4 lines, you output the type and number of ducks given, ordered like in the table:
# o	"Darth Vader Ducky: {count}
# Thor Ducky: {count}
# Big Blue Rubber Ducky: {count}
# Small Yellow Rubber Ducky: {count}"
# Constraints
# •	All the given numbers will be valid integers in the range [1, 1000].
# •	There will be no negative inputs.
# •	The number of values in both sequences will always be equal.

from collections import deque

programmer_time = deque(int(el) for el in input().split(' '))
given_tasks = [int(el) for el in input().split(' ')]

darth_vader = 0
thor = 0
big_blue = 0
small_yellow = 0

while programmer_time and given_tasks:
    current_programmer = programmer_time[0]
    current_task = given_tasks[-1]
    task_time = current_task*current_programmer
    if 0 <= task_time <= 60:
        darth_vader += 1
    elif 61 <= task_time <= 120:
        thor += 1
    elif 121 <= task_time <= 180:
        big_blue += 1
    elif 181 <= task_time <= 240:
        small_yellow += 1
    elif task_time > 240:
        given_tasks[-1] -= 2
        programmer_time.rotate(-1)
        continue
    programmer_time.popleft()
    given_tasks.pop()

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print(f"Darth Vader Ducky: {darth_vader}")
print(f"Thor Ducky: {thor}")
print(f"Big Blue Rubber Ducky: {big_blue}")
print(f"Small Yellow Rubber Ducky: {small_yellow}")

# --- Tests: ---
# Test1:
# 10 15 12 18 22 6
# 12 16 5 6 9 1
#
# Test2:
# 2 55 17 31 23
# 7 5 17 4 27
#
# --- Outputs: ---
# Test1:
# Congratulations, all tasks have been completed! Rubber ducks rewarded:
# Darth Vader Ducky: 1
# Thor Ducky: 3
# Big Blue Rubber Ducky: 1
# Small Yellow Rubber Ducky: 1
#
# Test2:
# Congratulations, all tasks have been completed! Rubber ducks rewarded:
# Darth Vader Ducky: 1
# Thor Ducky: 0
# Big Blue Rubber Ducky: 2
# Small Yellow Rubber Ducky: 2
