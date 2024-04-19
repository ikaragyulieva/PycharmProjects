# Create a generator function called possible_permutations() which should receive a list and return lists with all
# possible permutations between its elements.
# Note: Submit only the function in the judge system
import itertools


def possible_permutations(ls: list):
    # if len(ls) <= 1:
    #     yield ls
    # else:
    #     for el in range(len(ls)):
    #         for i in possible_permutations(ls[:el] + ls[el+1:]):
    #             yield [ls[el]] + i
    # second solution:
    for el in itertools.permutations(ls):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
