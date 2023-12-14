# First, you will be given two sequences of integer values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the following N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other.
# If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.

set_1 = set(int(x) for x in input().split(' '))
set_2 = set(int(x) for x in input().split(' '))

for _ in range(int(input())):
    command = input().split(' ')
    numbers = [int(num) for num in command[2:]]

    if command[0] == 'Add':
        if command[1] == 'First':
            set_1.update(numbers)
        else:
            set_2.update(numbers)
    elif command[0] == 'Remove':
        if command[1] == 'First':
            set_1.difference_update(numbers)
        else:
            set_2.difference_update(numbers)
    elif command[0] == 'Check':
        print(set_1.issubset(set_2) or set_2.issubset(set_1))

print(*sorted(set_1), sep=", ")
print(*sorted(set_2), sep=", ")
