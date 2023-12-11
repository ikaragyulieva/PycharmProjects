# You have an empty stack. You will receive an integer – N. On the following N lines, you will receive queries.
# Each query is one of these four types:
# · '1 {number}' – push the number (integer) into the stack
# · '2' – delete the number at the top of the stack
# · '3' – print the maximum number in the stack
# · '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"

n = int(input())

my_stack = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        my_stack.append(int(query[1]))
    elif my_stack:
        if query[0] == '2':
            my_stack.pop()
        elif query[0] == '3':
            print(max(my_stack))
        elif query[0] == '4':
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end='')
    if my_stack:
        print(', ', end='')
