# Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again.
# Farmers and gardeners plant their seeds and temperatures slowly rise.
# Write a function called start_spring which will receive a different number of keyword arguments.
# Each keyword holds a key with a name of the spring object (string), and each value holds its type (string).
# For example, dahlia="flower", shrikes="bird", dogwood="tree".
# The function should sort the given spring objects in collections by their type:
# •	The collections sorted by their number of elements in descending order. If two or more collections have the same
# number of elements in them, return them in ascending order (alphabetically) by the type's name.
# •	Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# Output
# •	Return the result, sorted as described above in the format:
# o	"{type_one}:
# -{spring_object_of_this_type_one}
# -{spring_object_of_this_type_two}
# …
# -{spring_object_of_this_type_N}
# {type_two}:
# …
# {type_N}:
# …
# -{last_spring_object_of_typeN}"

def start_spring(**kwargs):
    spring_collection = {}
    for element in kwargs.items():
        if element[1] not in spring_collection:
            spring_collection[element[1]] = []
        spring_collection[element[1]].append(element[0])
    sorted_collection = sorted(spring_collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''
    for spring_el, item in sorted_collection:
        result += f"{spring_el}:\n-"
        sorted_items = sorted(item)
        result += "\n-".join(el for el in sorted_items)
        result += "\n"

    return result


# --- Tests: ---
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

# --- Outputs: ---
# Test1:
# flower:
# -Dahlia
# -Tulip
# -Water Lilly
# bird:
# -Swallows
# -Swifts
# tree:
# -Callery Pear
#
# Test2:
# bird:
# -Shrikes
# -Swallow
# -Swallows
# -Thrushes
# -Warblers
# -Woodpeckers
#
# Test3:
# bird:
# -Shrikes
# -Swallow
# -Thrushes
# tree:
# -Cherries
# -Magnolia
# -Pear
# insect:
# -Butterfly


