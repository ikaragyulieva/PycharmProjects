# Write a function called operate that receives an operator ("+", "-", "*" or "/") as а first argument and multiple
# numbers (integers) as additional arguments (*args). The function should return the result of the operator applied
# to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

from functools import reduce

# def operate(sign, *args):
#
#     def add():
#         # return sum(args)
#         return reduce(lambda a, b: a+b, args)
#
#     def subtract():
#         # result = args[0]
#         # for index in range(1, len(args)):
#         #     result -= args[index]
#         # return result
#         return reduce(lambda a, b: a-b, args)
#
#     def multiply():
#         # result = 1
#         # for index in range(len(args)):
#         #     result *= args[index]
#         # return result
#         return reduce(lambda a, b: a*b, args)
#
#     def devide():
#         # result = 1
#         # for index in range(len(args)):
#         #     result /= args[index]
#         # return result
#         return reduce(lambda a, b: a/b, args)
#
#     if sign == '+':
#         return add()
#     elif sign == '-':
#         return subtract()
#     elif sign == '*':
#         return multiply()
#     elif sign == '/':
#         return devide()

# Solution with in one row:
def operate(sign, *args):
    return reduce(lambda a, b: eval(f"{a}{sign}{b}"), args)



print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))