# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

n = int(input())

unique_names = set()

for _ in range(n):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)



