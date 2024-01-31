# Write a concatenate() function that receives some strings as arguments and some named arguments
# (the key will be a string, and the value will be another string).
# First, you should concatenate all arguments successively. Next, take each key successively,
# and if it is present in the resulting string, change all matching parts with the key's value.
# In the end, return the final string.
#  See the examples for more clarification.
# Submit only your function in the judge system.

def concatenate(*args, **kwargs):
    word = ''
    for x in args:
        word += x
    for key, value in kwargs.items():
        if key in word:
            word = word.replace(key, value)

    return word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

