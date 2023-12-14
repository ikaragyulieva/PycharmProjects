# This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
# First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
# After that, you will be given another sequence of integers – their magic level.
# Your task is to mix materials with magic so you can craft presents,
# listed in the table below with the exact magic level:
#
# Present	Magic needed
# Doll	150
# Wooden train	250
# Teddy bear	300
# Bicycle 	400
#
# You should take the last box with materials and the first magic level value to craft a toy.
# Their multiplication calculates the total magic level.
# If the result equals one of the levels described in the table above, you craft the present and remove both materials
# and magic value. Otherwise:
# •	If the product of the operation is a negative number, you should sum the values together,
# remove them both from their positions and add the result to the materials.
# •	If the product doesn't equal one of the magic levels in the table and is a positive number,
# remove only the magic value and increase the material value by 15.
# •	If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
# Stop crafting presents when you run out of boxes of materials or magic level values.
# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle
# Input
# •	The first line of input will represent the values of boxes with materials - integers, separated by a single space
# •	On the second line, you will be given the magic values - integers again, separated by a single space
# Output
# •	On the first line - print whether you've succeeded in crafting the presents:
# o	"The presents are crafted! Merry Christmas!"
# o	"No presents this Christmas!"
# •	On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
# o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
# o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
# •	On the next lines print the presents you have crafted, ordered alphabetically in the format:
# o	"{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"
# Constraints
# •	All the materials' values will be integers in the range [-100, 100]
# •	Magic level values will be integers in the range [-100, 100]
# •	In all cases, at least one present will be crafted

from collections import deque

material = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
present = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
crafted_presents = {}


while material and magic:
    current_material = material[-1]
    current_magic = magic[0]
    if current_magic == 0 and current_material == 0:
        magic.popleft()
        material.pop()
        continue
    if current_magic == 0:
        magic.popleft()
        continue
    if current_material == 0:
        material.pop()
        continue

    product = current_material * current_magic
    if product < 0:
        product = current_material + current_magic
        material.pop()
        magic.popleft()
        material.append(product)
        continue
    present_is_crafted = False
    for key in present:
        if product == present[key]:
            if key not in crafted_presents:
                crafted_presents[key] = 0

            crafted_presents[key] += 1
            material.pop()
            magic.popleft()
            present_is_crafted = True
        if present_is_crafted:
            break
    if not present_is_crafted:
        magic.popleft()
        material[-1] += 15

if ('Doll' in crafted_presents.keys() and 'Train' in crafted_presents.keys()) or ('Teddy bear' in crafted_presents.keys() and 'Bicycle' in crafted_presents.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material:
    material.reverse()
    print(f"Materials left: {', '.join([str(x) for x in material])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for key, value in sorted(crafted_presents.items(), key=lambda kvp: kvp[0]):
    print(f"{key}: {value}")
