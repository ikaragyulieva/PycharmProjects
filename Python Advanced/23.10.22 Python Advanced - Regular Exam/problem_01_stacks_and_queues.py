# John is quite an avid off-road fan. He bought a new jeep and made the necessary improvements to it.
# John is ready for new off-road adventures and can't wait to get started.
# In this challenge, he must save his fuel very carefully…
# There will be two sequences of integers. The first sequence will represent the initial fuel and the second -
# additional consumption index due to thin air at high altitudes, hence higher fuel consumption.
# There will also be a third sequence of integers, representing values equal to the necessary amount of fuel needed to
# reach the corresponding altitude in the challenge.
# Your task is to take the last fuel quantity from the fuel sequence and the first index from the additional
# consumption index sequence. Subtract the values and check the result.
# •	The corresponding altitude is reached if the calculated result is bigger or equal to the first element from the
# needed amount of fuel sequence. You need to remove both the fuel and the consumption index from their sequences as
# well as the needed amount of fuel index from their sequence.
# •	If the calculated result is smaller or not equal to the first element from the needed amount of fuel sequence,
# the corresponding altitude is not reached, movement cannot continue, and the program should end.
# Input
# •	The first line will represent the initial fuel – integers, separated by a single space.
# •	The second line will represent the consumption indexes that decrease initial fuel –
# integers, separated by a single space.
# •	The third line will represent the quantities needed to reach the corresponding altitude –
# integers, separated by a single space.
# Output
# •	On the first or the next n lines, output the corresponding message on the console from the following options:
# 	If John reaches the altitude, print the message:
# o	"John has reached: Altitude 1"
# o	…
# o	"John has reached: Altitude {n}"
# 	If John fails to reach the altitude, print the message:
# o	"John did not reach: Altitude {n}"
# •	On the next lines, based on whether he reached the top or not,
# print the following on the console in the specified format:
# 	If John doesn't have enough fuel to reach the top but has reached some altitude, display the following messages:
# o	"John failed to reach the top.
# Reached altitudes: Altitude 1, … Altitude {n}"
# 	If John does not have enough fuel to reach the top and has not reached any altitude, print:
# o	"John failed to reach the top.
# John didn't reach any altitude."
# 	If John manages to reach all the altitudes, he will reach the top.
# End the program and print on the console the following message:
# o	"John has reached all the altitudes and managed to reach the top!"
# Constraints
# •	All the given numbers will be valid integers in the range [1, 200].
# •	All sequences always consist of four elements.
# •	There will be no negative input.


from collections import deque

fuel = [int(x) for x in input().split(' ')]
additional_consumption = deque(int(x) for x in input().split(' '))
needed_fuel = deque(int(x) for x in input().split(' '))
conquered_altitudes = []
index = 0

while additional_consumption and fuel:
    current_consumption = additional_consumption[0]
    current_fuel = fuel[-1]
    current_race = current_fuel - current_consumption
    if current_race >= needed_fuel[0]:
        index += 1
        conquered_altitudes.append(f'Altitude {index}')
        print(f"John has reached: Altitude {index}")
        fuel.pop()
        additional_consumption.popleft()
        needed_fuel.popleft()
    else:
        print(f"John did not reach: Altitude {index+1}")
        break

if not needed_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
elif index == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif index > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(el for el in conquered_altitudes)}")

# --- Tests: ---
# Test1:
# 200 90 40 100
# 20 40 30 50
# 50 60 80 90
#
# Test2:
# 40 66 123 100
# 10 30 70 33
# 40 55 77 100
#
# Test3:
# 199 190 100 100
# 20 40 30 50
# 50 60 70 80
#
# --- Outputs: ---
# Test1:
# John has reached: Altitude 1
# John did not reach: Altitude 2
# John failed to reach the top.
# Reached altitudes: Altitude 1
#
# Test2:
# John has reached: Altitude 1
# John has reached: Altitude 2
# John did not reach: Altitude 3
# John failed to reach the top.
# Reached altitudes: Altitude 1, Altitude 2
#
# Test3:
# John has reached: Altitude 1
# John has reached: Altitude 2
# John has reached: Altitude 3
# John has reached: Altitude 4
# John has reached all the altitudes and managed to reach the top!
