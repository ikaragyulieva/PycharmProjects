 # Unpacking
# num = [1, 2, 3]
# a, b, c = num
#
# print(a)
# print(b)
# print(c)

# Sets:
a = {1, 2, 3, 4,}
b = {3, 4, 5, 6}

union = a | b
intersection = a & b
subset = a < b
superset = a > b
difference = a - b
symetric_difference = a ^ b

print(union)
print(intersection)
print(subset)
print({1,2} < {1,2,3})
print(difference)
print(symetric_difference)