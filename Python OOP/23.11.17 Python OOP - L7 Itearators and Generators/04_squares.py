# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).

def squares(n):
    index = 1
    while index <= n:
        yield index * index
        index += 1


print(list(squares(5)))
