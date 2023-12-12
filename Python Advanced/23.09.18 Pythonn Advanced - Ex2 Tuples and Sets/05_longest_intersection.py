# Write a program that finds the longest intersection.
# You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.


n = int(input())

longest_intersection = set()

for _ in range(n):
    range_1, range_2 = input().split('-')
    start_1, finish_1 = [int(x) for x in range_1.split(',')]
    start_2, finish_2 = [int(x) for x in range_2.split(',')]

    first_set = set(range(start_1, finish_1+1))
    second_set = set(range(start_2, finish_2+1))

    intersection = first_set & second_set

    if  len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')