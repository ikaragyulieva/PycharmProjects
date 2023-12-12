# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.


# Solution 1:
# nums = tuple(float(el) for el in input().split())
# occ = {}
#
# for num in nums:
#     occ[num] = nums.count(num)
#
# for key, value in occ.items():
#     print(f"{key} - {value} times")

# Solution 2

nums = tuple(float(el) for el in input().split())
occ = {}

for num in nums:
    if num not in occ:
        occ[num] = nums.count(num)
        print(f"{num} - {nums.count(num)} times")
