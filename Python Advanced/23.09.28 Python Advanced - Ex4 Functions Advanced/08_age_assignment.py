# Create a function called age_assignment() that receives a different number of names and a different number of
# key-value pairs. The key will be a single letter (the first letter of each name) and the value - a number (age).
# Find its first letter in the key-value pairs for each name and assign the age to the person's name.
# Then, sort the names in ascending order (alphabetically) and return the information for each person on a new line in
# the format: "{name} is {age} years old."
# Submit only the function in the judge system.

def age_assignment(*args, **kwargs):
    assignment = {}
    result = []
    for name in args:
        for letter, age in kwargs.items():
            if letter == name[0]:
                assignment[name] = age
                break
    sorted_assignment = sorted(assignment.items(), key=lambda kvp: kvp[0])
    for name, age in sorted_assignment:
        result.append(f"{name} is {age} years old.")
    return '\n'.join(result)

# --- Optimised solution ---

# def age_assignment(*args, **kwargs):
#     persons = {}
#     for name in args:
#         persons[name] = kwargs[name[0]]
#     result = sorted(persons.items(), key=lambda kvp: kvp[0])
#     final_result = []
#     for name, age in result:
#         final_result.append(f"{name} is {age} years old")
#     return '\n'.join(final_result)


# --- Tests: ---

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
