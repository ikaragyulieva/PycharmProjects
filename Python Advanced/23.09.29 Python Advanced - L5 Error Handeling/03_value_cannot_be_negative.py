# Create your own exception called ValueCannotBeNegative. Write a program that reads five numbers from the console
# (on separate lines). If a negative number occurs, raise the exception.
class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative
