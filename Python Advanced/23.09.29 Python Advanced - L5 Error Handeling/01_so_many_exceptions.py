# You are provided with the following code. This code raises many exceptions. Fix it, so it works correctly.
# It is given a sequence of numbers, separated by a ", ". Iterate through each number by its index, and if the number is
# smaller or equal to 5, make a multiplication. If the number is larger than 5 and smaller or equal to 10, divide the
# result by the number. In the end, print the final result.
# Hints
# First, let us start the program, to see the first exception we will hit:
# # It is a SyntaxError on line 6 of our code. It is missing the ":" sign. Let us add it and again run the program:
# When we put the input code, the program raises a ValueError on line 1.
# It says that the input data is not of type "int". So, to escape the error, we should remove the int() converter and a\
# gain run the program:
# Now, the program raises a TypeError on line 4. It says that the list cannot be interpreted as an integer.
# As you know, when we want to use the range() function, we should give it a start value (integer), an end value
# (integer), and a step value (integer). However, is given a list as an argument of that function. We should change it,
# as we want to use the index of the list, not the elements in it. Then, run the program again:
# The program raises a TypeError on line 6. It says that the conditional operator cannot be supported between str and
# int values. As we can see, the int value is 5, so the string value (number) should be changed to an integer.
# Let us change all elements in the list to integers at the beginning of the program:
# The program now raises an IndexError on line 5. It says that the index is out of the listed range.
# We can debug that and see that when the "i" value is the last index (2 in this test), the program tries to reach the
# 3rd index of the list that does not exist. In this case, we want to remove the additional summation of the index:
# Now, the program raises a NameError on line 11 saying that the name "total" is not defined.
# Let us remove that error by adding the right variable name - "result":
# We can see that now we receive the right output and the program finishes with code 0.

# numbers_list = int(input()).split(", ")
# result = 1
# for i in range(numbers_list):
#   number = numbers_list[i+1]
# if number <= 5
#   result *= number
# elif 5 < number <= 10:
#    result /= number
# print(total)

numbers_list = [int(x) for x in input().split(", ")]
result = 1
for i in range(len(numbers_list)):
    number = numbers_list[i]
if number <= 5:
    result *= number
elif 5 < number <= 10:
    result /= number
print(result)