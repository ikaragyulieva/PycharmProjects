# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
# If the user passes a non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")

try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")

