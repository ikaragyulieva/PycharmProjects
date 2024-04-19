# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
# The first two numbers in the sequence are always 0 and 1.
# Each following Fibonacci number is created by the sum of the current number with the previous one.
# Note: Submit only the function in the judge system

def fibonacci():
    num_2 = 1
    fibonacci_num = 0
    while True:
        yield fibonacci_num
        fibonacci_num, num_2 = num_2, fibonacci_num + num_2





# Tests:
generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
