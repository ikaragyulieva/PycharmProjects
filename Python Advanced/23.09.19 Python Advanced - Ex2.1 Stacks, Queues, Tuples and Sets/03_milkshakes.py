# You are learning how to make milkshakes.
# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start with the last chocolate and try to match it with the first cup of milk. If their values are equal,
# you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the
# sequence and decrease the value of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0,
# you should remove them from the records right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left,
# you need to stop making chocolate milkshakes.
# Input
# •	On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
# •	On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
# •	On the first line, print:
# o	If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
# o	Otherwise: "Not enough milkshakes."
# •	On the second line - print:
# o	If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
# o	Otherwise: "Chocolate: empty"
# •	On the third line - print:
# o	If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
# o	Otherwise: "Milk: empty"
# Constraints
# •	All given numbers will be valid integers in the range [-100 … 100].

from collections import deque

chocolate = [int(ch) for ch in input().split(', ')]
milk_cups = deque(int(i) for i in input().split(', '))
milkshakes_done = 0

while chocolate and milk_cups and milkshakes_done < 5:
    if chocolate[-1] <= 0 and milk_cups[0] <= 0:
        chocolate.pop()
        milk_cups.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    elif chocolate[-1] == milk_cups[0]:
        milkshakes_done += 1
        chocolate.pop()
        milk_cups.popleft()
    else:
        milk_cups.rotate(-1)
        chocolate[-1] -= 5


if milkshakes_done >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
# if chocolate:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
# else:
#     print("Chocolate: empty")
# if milk_cups:
#     print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
# else:
#     print("Milk: empty")
print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk_cups]) if milk_cups else 'empty'}")
