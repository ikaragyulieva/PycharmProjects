# Maria wants to make a firework show for the wedding of her best friend.
# We should help her to make the perfect firework show.
#
# First, you will be given a sequence of integers representing firework effects.
# Afterward you will be given another sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power.
# If the sum of their values is:
# •	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# •	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# •	divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence.
# Then, try to mix the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show, or you have no more firework punches
# or explosive power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
# Input
# •	On the first line, you will receive the integers representing the firework effects, separated by ", ".
# •	On the second line, you will receive the integers representing the explosive power, separated by ", ".
# Output
# •	On the first line, print:
# o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
# o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# •	On the second line, print all firework effects left if there are any:
# o	"Firework Effects left: {effect1}, {effect2}, (…)"
# •	On the third line, print all explosive fillings left if there are any:
# o	" Explosive Power left: {filling1}, {filling2}, (…)"
# •	Then, you need to print all fireworks and the amount you have of them:
# o	"Palm Fireworks: {count}"
# o	"Willow Fireworks: {count}"
# o	"Crossette Fireworks: {count}"
# Constraints
# •	All the given numbers will be integers in the range [-100, 100].
# •	There will be no cases with empty sequences.

from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]
palm_firework = 0
willow_firework = 0
crossette_firework = 0
enough_fireworks = False

while firework_effects and explosive_power and not enough_fireworks:

    current_firework_effect = firework_effects[0]
    current_explosive_power = explosive_power[-1]
    if current_explosive_power <= 0 and current_firework_effect <= 0:
        firework_effects.popleft()
        explosive_power.pop()
        continue
    elif current_explosive_power <= 0:
        explosive_power.pop()
        continue
    elif current_firework_effect <= 0:
        firework_effects.popleft()
        continue

    fireworks_mix = current_firework_effect + current_explosive_power

    if fireworks_mix % 3 == 0 and fireworks_mix % 5 != 0:
        palm_firework += 1
    elif fireworks_mix % 3 != 0 and fireworks_mix % 5 == 0:
        willow_firework += 1
    elif fireworks_mix % 3 == 0 and fireworks_mix % 5 == 0:
        crossette_firework += 1
    else:
        firework_effects[0] -= 1
        firework_effects.rotate(-1)
        continue

    firework_effects.popleft()
    explosive_power.pop()

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        enough_fireworks = True

if enough_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")


# --- Tests ---
# Test1
# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

# Test2:
# -15, -8, 0, -16, 0, -22
# 10, 5

# --- Outputs ---
# Test1
# Congrats! You made the perfect firework show!
# Palm Fireworks: 4
# Willow Fireworks: 3
# Crossette Fireworks: 3


# Test2
# Sorry. You can't make the perfect firework show.
# Explosive Power left: 10, 5
# Palm Fireworks: 0
# Willow Fireworks: 0
# Crossette Fireworks: 0


