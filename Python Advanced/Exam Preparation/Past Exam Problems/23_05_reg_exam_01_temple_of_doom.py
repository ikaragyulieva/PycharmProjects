# Harry will have to discover an important artifact in a cursed temple. Relying on the inscriptions at the entrance,
# Harry realizes that he will have to face unprecedented challenges.
# He must take all the useful things that he has in his truck...
# There will be given two sequences of integers, representing tools and substances that he has at his disposal.
# There will also be a third sequence of integers, representing all challenges in the temple.
# Your task is to take the first tool from the tools sequence and the last substance from the substances sequence.
# Multiply the values and check the result.
# •	If the calculated result is equal to any of the elements from the challenges sequence, the challenge is resolved.
# You need to remove both the tool and the substance from their sequences.
# The challenge should also be removed from its sequence.
# •	If the calculated result is not equal to any of the elements from the challenges sequence,
# the challenge is not resolved:
# o	Increase the value of the tool element by 1 and move the element to the back of the tools’ sequence.
# o	Decrease the value of the substance element by 1 and return the element to the substance’s sequence.
# If the value of the substance element reaches 0, remove it from the sequence.
# If Harry has no substances or tools left (the substances sequence is empty) but has more challenges to resolve,
# he is lost in the temple forever. End the program and print on the console the following message:
# •	"Harry is lost in the temple. Oblivion awaits him."
# If Harry manages to pass all the challenges, he will find the artifact.
# End the program and print on the console the following message:
# •	"Harry found an ostracon, which is dated to the 6th century BCE."
# Input
# •	The first line will represent the tools that Harry has at his disposal – integers, separated by a single space.
# •	The second line will represent the substances that Harry has at his disposal –
# integers, separated by a single space.
# •	The third line will represent the challenges that Harry will have to resolve –
# integers, separated by a single space.
# Output
# •	On the first line print on the console the appropriate message, among the following:
# o	"Harry is lost in the temple. Oblivion awaits him."
# o	"Harry found an ostracon, which is dated to the 6th century BCE."
# •	On the next three lines, print on the console the elements of the non-empty sequences, in the following format:
# o	"Tools: element1, element2, element3 … element n"
# o	"Substances: element1, element2, element3 … element n"
# o	"Challenges: element1, element2, element3 … element n"
# Constraints
# •	All the given numbers will be valid integers in the range [1, 100].
# •	There will be no negative inputs.

from collections import deque

tools = deque(int(x) for x in input().split(' '))
substances = [int(x) for x in input().split(' ')]
challenges = [int(x) for x in input().split(' ')]

while substances and tools:
    current_substance = substances[-1]
    current_tool = tools[0]
    power = current_tool * current_substance
    if power in challenges:
        challenges.remove(power)
        substances.pop()
        tools.popleft()
    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")

# --- Tests: ---
# Test1:
# 2 4 6 8
# 11 3 5 7 9
# 24 28 18 30
#
# Test2:
# 13 7 4 22 11 15 20
# 3 2 1
# 12 10 5
#
#
# --- Outputs: ---
# Test1:
# Harry found an ostracon, which is dated to the 6th century BCE.
# Substances: 11
#
# Test2:
# Harry is lost in the temple. Oblivion awaits him.
# Tools: 20, 14, 8, 5, 23, 12, 16
# Challenges: 12, 10, 5
