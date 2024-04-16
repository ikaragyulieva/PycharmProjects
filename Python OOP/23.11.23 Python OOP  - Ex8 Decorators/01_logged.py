# Create a decorator called logged. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called.
# See the examples for more clarification.
# Hints
# •	Use {func}.__name__ to get the name of the function
# •	Call the function to get the result
# •	Return the result

def logged(function):

    def wrapped(*args, **kwargs):
        func_name = function.__name__ + str(args)
        result = function(*args, **kwargs)
        return f"you called {func_name}\nit returned {result}"

    return wrapped


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
