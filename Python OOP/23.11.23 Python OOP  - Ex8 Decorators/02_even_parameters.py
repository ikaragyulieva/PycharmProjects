# Create a decorator function called even_parameters. It should check if all parameters passed to a function are even
# numbers and only then execute the function and return the result.
# Otherwise, don't execute the function and return "Please use only even numbers!"

def even_parameters(function):
    def wrapped(*args):
        for el in args:
            if not isinstance(el, int) or el % 2 != 0:
                return "Please use only even numbers!"

        # second solution
        # if any(not isinstance(el, int) or el % 2 != 0 for el in args):
        #     return "Please use only even numbers!"

        return function(*args)

    return wrapped


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
