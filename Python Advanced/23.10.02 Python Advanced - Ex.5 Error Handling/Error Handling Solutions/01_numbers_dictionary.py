numbers_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break
    if line != "Search":
        try:
            number_as_string = line
            number = int(input())
            numbers_dictionary[number_as_string] = number
        except ValueError:
            print("The variable number must be an integer")

line = input()
while True:
    if line == "Remove":
        break
    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while True:
    if line == "End":
        break
    try:
        del numbers_dictionary[line]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)

