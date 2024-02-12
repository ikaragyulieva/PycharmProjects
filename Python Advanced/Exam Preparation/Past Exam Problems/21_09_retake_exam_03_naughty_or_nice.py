# Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents,
# so Santa Claus is preparing his list this year to check which child has been good or bad.
# Write a function called naughty_or_nice_list which will receive
# •	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
# •	A different number of arguments (strings) and/or keywords representing commands
# The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
# The list holds a different number of kids - tuples containing two elements: a counting number (integer)
# at the first position and a name (string) at the second position.
# For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
# Next, the function could receive arguments and/or keywords.
# Each argument is a command. The commands could be the following:
# •	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a
# list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
# •	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list
# with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
# Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
# •	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
# depending on the value in the keyword. Then, remove it from the Santa list.
# •	Otherwise, ignore the command.
# All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
# In the end, return the final lists, each on a new line as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# •	The function should return strings with the names on each list on separate lines, if there are any,
# otherwise skip the line:
# o	"Nice: {name1}, {name2} … {nameN}"
# o	"Naughty: {name1}, {name2} … {nameN}"
# o	"Not found: {name1}, {name2} … {nameN}"

def naughty_or_nice_list(kids, *args, **kwargs):
    naughty_kids = []
    nice_kids = []

    for command in args:
        num, status = command.split('-')
        num = int(num)
        unique_kid = False
        name = None
        for kid_num, kid_name in kids:
            if kid_num == num and unique_kid:
                unique_kid = False
                break
            if kid_num == num:
                name = kid_name
                unique_kid = True
        if unique_kid:
            kids.remove((num, name))
            if status == 'Naughty':
                naughty_kids.append(name)
            else:
                nice_kids.append(name)

    for name, status in kwargs.items():
        unique_kid = False
        num = 0
        for kid_num, kid_name in kids:
            if kid_name == name and unique_kid:
                unique_kid = False
                break
            if kid_name == name:
                unique_kid = True
                num = kid_num

        if unique_kid:
            kids.remove((num, name))
            if status == 'Naughty':
                naughty_kids.append(name)
            else:
                nice_kids.append(name)

    not_found = [name for _, name in kids]
    result = ''
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"

    return result


# --- Tests: ---
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

# --- Outputs: ---
# Test1:
# Nice: Amy
# Naughty: Tom, Katy
# Not found: George
#
# Test2:
# Nice: Simon, Peter, Lilly
# Not found: Peter, Peter
#
# Test3:
# Nice: Karen, Tim, Frank
# Naughty: Merry, John
