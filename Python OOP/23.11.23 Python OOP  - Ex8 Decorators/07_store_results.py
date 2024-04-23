# Create a class called store_results. It should be used as a decorator and store information about the executed
# functions in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"
# Note: The solutions to this problem cannot be submitted in the judge system

def store_results(function):
    def wrapper(*args):
        with open('result.txt', 'a') as result_file:
            result_file.write(f"Function '{function.__name__}' was called. Result: {function(*args)}\n")
    return wrapper


# solution with class:
# class store_results:
#     def __init__(self, function):
#         self.func = function
#
#     def __call__(self, *args, **kwargs):
#         with open('result.txt', 'a') as result_file:
#             result_file.write(f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}\n")
#

@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
