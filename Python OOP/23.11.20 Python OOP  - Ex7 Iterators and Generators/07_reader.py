# Create a generator function called read_next() which should receive a different number of arguments (all iterable).
# On each iteration, the function should return each element from each sequence.
# Note: Submit only the function in the judge system

def read_next(*args):
    for i in args:
        # for el in i:
        #     yield el
        # --- 2nd solution:---
        yield from i


# Tests:
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
