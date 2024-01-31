# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.
# Submit only your function in the judge system.

def even_odd(*args):

    command = args[-1]
    result = []

    for number in range(len(args)-1):
        if command == 'even' and args[number] % 2 == 0:
            result.append(args[number])
        elif command == 'odd' and args[number] % 2 != 0:
            result.append(args[number])

    return result

# --- Alternative solution 1 ---
#     if command == 'even':
#         return list(filter(lambda x: x % 2 == 0, args[:-1]))
#     return list(filter(lambda x: x % 2 != 0, args[:-1]))


# --- Alternative solution 2 ---
#     if command == 'even':
#         return list(x for x in args[:-1] if x % 2 == 0)
#     return list(x for x in args[:-1] if x % 2 != 0)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))