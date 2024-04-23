# Import the time module. Create a decorator called exec_time.
# It should calculate how much time a function needs to be executed. See the examples for more clarification.
# Note: You might have different results from the given ones.
# The solutions to this problem cannot be submitted in the judge system.
# •	Use the time library to start a timer
# •	Execute the function
# •	Stop the timer and return the result

import time


def exec_time(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()

        return end_time - start_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1


print(loop())
