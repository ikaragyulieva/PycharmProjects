# 1.	Bombs
# Link to Judge: https://judge.softuni.org/Contests/Practice/Index/2456#0
# Ezio is still learning how to make bombs. With their help, he will save civilization.
# We should help Ezio to make his perfect bombs.
# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing.
# If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the
# value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop
# combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# •	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# •	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# •	On the first line, print:
# o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# •	On the second line, print all bomb effects left:
# o	If there are no bomb effects: "Bomb Effects: empty"
# o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# •	On the third line, print all bomb casings left:
# o	If there are no bomb casings: "Bomb Casings: empty"
# o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# •	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o	"Cherry Bombs: {count}"
# o	"Datura Bombs: {count}"
# o	"Smoke Decoy Bombs: {count}"
# Constraints
# •	All given numbers will be valid integers in the range [0, 120].
# •	There will be no cases with negative material.

from collections import deque

bomb_effects = deque(int(el) for el in input().split(', '))
bomb_casings = [int(el) for el in input().split(', ')]
datura_bombs = 0
cherry_bombs = 0
smoke_bombs = 0
pouch_is_filled = False

while bomb_effects and bomb_casings and not pouch_is_filled:
    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]

    bomb_mix = current_effect + current_casing
    if bomb_mix == 40:
        datura_bombs += 1
    elif bomb_mix == 60:
        cherry_bombs += 1
    elif bomb_mix == 120:
        smoke_bombs += 1
    else:
        bomb_casings[-1] -= 5
        continue
    bomb_effects.popleft()
    bomb_casings.pop()

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_bombs >= 3:
        pouch_is_filled = True

if pouch_is_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_bombs}")


# Link to Judge: https://judge.softuni.org/Contests/Practice/Index/2456#0
# --- Tests: ---
# Test1:
# 5, 25, 25, 115
# 5, 15, 25, 35
#
# Test2:
# 30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
# 20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10

# --- Outputs: ---
# Test1:
# You don't have enough materials to fill the bomb pouch.
# Bomb Effects: empty
# Bomb Casings: empty
# Cherry Bombs: 0
# Datura Bombs: 3
# Smoke Decoy Bombs: 1

# Test2:
# Bene! You have successfully filled the bomb pouch!
# Bomb Effects: 100, 80
# Bomb Casings: 20
# Cherry Bombs: 3
# Datura Bombs: 4
# Smoke Decoy Bombs: 3
