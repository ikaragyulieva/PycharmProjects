# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received.
# For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
# •	By values in descending order, if the sum of all values of the dictionary is odd
# •	By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just any number of words passed to your function
# Output
# •	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
# Constraints:
# •	There will be no case with capital letters.
# •	There will be no case with a string consisting of other than letters.


def words_sorting(*args):
    words = {}
    result = []
    for item in args:
        if item not in words:
            words[item] = 0
        words[item] = sum(map(ord, item))

    if sum(words.values()) % 2 == 0:
        for item in sorted(words.items(), key=lambda kvp: (kvp[0])):
            result.append(f"{item[0]} - {item[1]}")
    else:
        for item in sorted(words.items(), key=lambda kvp: (-kvp[1])):
            result.append(f"{item[0]} - {item[1]}")

    return '\n'.join(result)


# --- Tests: ---
# Test1:
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

# Test2:
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

# Test3:
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))

# --- Outputs: ---
# Test1:
# charm - 523
# escape - 625
# mythology - 1004
#
# Test2:
# escape - 625
# charm - 523
# eye - 323
#
# Test3:
# accolade - 812
# cacophony - 964
