# Your friend Stamat is working on a new AI program. Like every irresponsible teenager, he programs all night and,
# of course, drinks a lot of energy drinks. Stamat's friends are concerned about him and want you to create a program
# that tells him when to stop the energy drinks and start drinking water.
# On the first line, you will receive a sequence of numbers representing milligrams of caffeinе. On the second line,
# you will receive another sequence of numbers representing energy drinks. It is important to know that the maximum
# caffeine Stamat can have for the night is 300 milligrams, and his initial is always 0.
# To calculate the caffeine in the drink take the last milligrams of caffeinе and the first energy drink, and multiply
# them. Then, compare the result with the caffeine Stamat drank:
# •	If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams, remove
# both the milligrams of caffeinе and the drink from their sequences. Also, add the caffeine to Stamat's total caffeine.
# •	If Stamat is about to exceed his maximum caffeine per night, do not add the caffeine to Stamat’s total caffeine.
# Remove the milligrams of caffeinе and move the drink to the end of the sequence. Also, reduce the current caffeine
# that Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).
# Stop calculating when you are out of drinks or milligrams of caffeine.
# For more clarification, see the examples below.
# Input
# •	In the first line, you will be given a sequence of the milligrams of caffeinе -
# integers separated by comma and space ", " in the range [1, 50]
# •	In the second line, you will be given a sequence of energy drinks -
# integers separated by comma and space ", " in the range [1, 300]
# Output
# •	On the first line:
# o	If Stamat hasn't drunk all the energy drinks, print the remaining ones separated by a comma and a space ", ":
# 	"Drinks left: { remaining drinks separated by ", " }"
# o	If Stamat has drunk all the energy drinks, print:
# 	"At least Stamat wasn't exceeding the maximum caffeine."
# •	On the next line, print:
# o	"Stamat is going to sleep with { current caffeine } mg caffeine."
# Constraints
# •	You will always have at least one element in each sequence at the beginning.

from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
caffeine_taken = 0
while caffeine and energy_drinks:
    current_caffeine = caffeine[-1]
    current_drink = energy_drinks[0]
    drink_caffeine = current_drink * current_caffeine
    if drink_caffeine + caffeine_taken <= 300:
        caffeine_taken += drink_caffeine
        caffeine.pop()
        energy_drinks.popleft()
    else:
        caffeine.pop()
        energy_drinks.rotate(-1)
        caffeine_taken -= 30
        if caffeine_taken < 0:
            caffeine_taken = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(str(el) for el in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_taken} mg caffeine.")


# --- Tests: ---
# Test1:
# 34, 2, 3
# 40, 100, 250
#
# Test2:
# 1, 16, 8, 14, 5
# 27, 23
#
# Test3:
# 1, 23, 2, 1, 42, 22, 7, 14
# 51, 100, 3, 7
#
# --- Outputs: ---
# Test1:
# Drinks left: 100, 250
# Stamat is going to sleep with 60 mg caffeine.
#
# Test2:
# At least Stamat wasn't exceeding the maximum caffeine.
# Stamat is going to sleep with 289 mg caffeine.
#
# Test3:
# At least Stamat wasn't exceeding the maximum caffeine.
# Stamat is going to sleep with 264 mg caffeine.
