# Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine.
# He asks Genie for help to prepare the wedding presents.
# First, you will receive a sequence of integers representing the materials for every wedding present.
# After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
# Your task is to mix materials with magic levels, so you can make presents, listed in the table below.
# Gift	Magic needed
# Gemstone	100 to 199
# Porcelain Sculpture	200 to 299
# Gold	300 to 399
# Diamond Jewellery	400 to 499
# To make a present, you should take the last integer of materials and sum it with the first magic level value.
# If the result is between or equal to the numbers described in the table above,
# you make the corresponding gift and remove both materials and magic value. Otherwise:
# •	If the product of the operation is under 100:
# o	And if it is an even number, double the materials, and triple the magic, then sum it again.
# o	And if it is an odd number, double the sum of the materials and the magic level.
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2.
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If, however, the result is not between or equal to any of the numbers in the table above after performing
# the calculation, remove both the materials and the magic level.
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs -
# a gemstone and a sculpture or gold and jewellery.
# Input
# •	The first line of input will represent the values of materials - integers, separated by a single space
# •	On the second line, you will be given the magic levels - integers, separated by a single space
# Output
# •	On the first line - print whether you have succeeded in crafting the presents:
# o	"The wedding presents are made!"
# o	"Aladdin does not have enough wedding presents."
# •	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
# o	"Materials left: {material1}, {material2}, …"
# o	"Magic left: {magicValue1}, {magicValue2}, …
# •	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
# "{present1}: {amount}
# {present2}: {amount}
# …
# {presentN}: {amount}"
# Constraints
# •	All the materials values will be integers in the range [1, 1000]
# •	Magic level values will be integers in the range [1, 1000]

from collections import deque


def present_making(magic, materials_list, magics_list):
    present_made = ''
    if 100 <= magic < 200:
        present_made = 'Gemstone'
    elif 200 <= magic < 300:
        present_made = 'Porcelain Sculpture'
    elif 300 <= magic < 400:
        present_made = 'Gold'
    elif 400 <= magic < 500:
        present_made = 'Diamond Jewellery'
    materials_list.pop()
    magics_list.popleft()
    return present_made


materials = [int(x) for x in input().split(' ')]
magics = deque(int(x) for x in input().split(' '))
crafted_gifts = {}


while materials and magics:
    current_material = materials[-1]
    current_magic = magics[0]
    present_magic = current_material + current_magic

    if present_magic < 100:
        if present_magic % 2 == 0:
            present_magic = (current_material * 2) + (current_magic * 3)
        else:
            present_magic += present_magic

    if present_magic > 499:
        present_magic /= 2

    if 100 > present_magic or present_magic > 499:
        materials.pop()
        magics.popleft()
        continue

    present = present_making(present_magic, materials, magics)
    if present not in crafted_gifts.keys():
        crafted_gifts[present] = 0
    crafted_gifts[present] += 1


if (('Gemstone' in crafted_gifts and 'Porcelain Sculpture' in crafted_gifts)
        or ('Gold' in crafted_gifts and 'Diamond Jewellery' in crafted_gifts)):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for item in sorted(crafted_gifts.items(), key=lambda kvp: kvp[0]):
    print(f"{item[0]}: {item[1]} ")


# --- Tests ---
# Test1:
# 105 20 30 25
# 120 60 11 400 10 1
#
# Test2:
# 30 5 21 6 0 91
# 15 9 5 15 8
#
# Test3:
# 200
# 5 15 32 20 10 5

# --- Outputs ---
# Test1:
# The wedding presents are made!
# Magic left: 10, 1
# Gemstone: 1
# Porcelain Sculpture: 2
#
# Test2:
# Aladdin does not have enough wedding presents.
# Materials left: 30
# Gemstone: 1
#
# Test3:
# Aladdin does not have enough wedding presents.
# Magic left: 15, 32, 20, 10, 5
# Porcelain Sculpture: 1
