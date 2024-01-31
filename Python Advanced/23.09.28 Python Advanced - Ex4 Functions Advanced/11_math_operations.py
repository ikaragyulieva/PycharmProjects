# Write a function named math_operations that receives a different number of floats as arguments and 4keyword arguments.
# The keys will be single letters: "a", "s", "d", and "m", and the values will be numbers.
# You need to take each float argument from the sequence and do mathematical operations as follows:
# •	The first element should be added to the value of the key "a"
# •	The second element should be subtracted from the value of the key "s"
# •	The third element should be divisor to the value of the key "d"
# •	The fourth element should be multiplied by the value of the key "m"
# •	Each result should replace the value of the corresponding key
# •	You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error,
# you should skip the operation and continue to the next one.
# After you finish calculating all numbers, sort the four elements by their values in descending order.
# If two or more values are equal, sort them by their keys in ascending order (alphabetically).
# In the end, return each key-value pair in the format "{key}: {value}" on separate lines.
# Each value should be formatted to the first decimal point.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# •	All of the given numbers will be valid integers in the range [-100, 100]
# Output
# •	The function should return the final dictionary

