# You are hired to create a program that implements SJF (Shortest Job First).
# It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.
# On the first line you will be given the jobs as integers (clock-cycles needed to finish the job)
# separated by comma and space ", ". On the second line you will be given the index of the job that we are interested
# in and want to know how many cycles will pass until the job is done.
# The tasks that need the least amount of clock-cycles will be completed first.
# For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
# You have to print how many clock-cycles will pass until the task you are interested in is completed.
# For more clarifications, see the examples below.
# Input
# •	On the first line you will receive numbers separated by ", "
# •	On the second line you will receive the index of the task you are interested in
# Output
# •	Single line: the clock-cycles that will pass until the task you are interested in is finished

# https://judge.softuni.org/Contests/2551/Python-Advanced-Exam-24-October-2020

from collections import deque

numbers = [int(el) for el in input().split(', ')]
task_index = int(input())

cycles = 0
jobs = deque()
task_is_not_done = True

for el in range(len(numbers)):
    jobs.append([numbers[el], el])
print(jobs)
while task_is_not_done:
    smallest_element = jobs[0][0]
    smallest_index = jobs[0][1]
    index = 0
    for job in range(len(jobs)):
        if jobs[0][0] < smallest_element:
            smallest_element = jobs[0][0]
            smallest_index = jobs[0][1]
            index = job

        jobs.rotate(-1)

    cycles += smallest_element
    del jobs[index]

    if smallest_index == task_index:
        task_is_not_done = False
        print(cycles)
