# The task is not included in the Judge system.
# You will receive a sequence of numbers (unique integers) separated by space on the first line.
# On the second line, you'll receive a target number.
# Your task is to find the pairs of numbers whose sum equals the target number.
# For each found pair print "{number} + {number} = {target_number}".
# You should NOT use the same element twice to fulfill the condition above.
# Can you come up with an algorithm that has less time complexity?

n = int(input())

cars = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        if car_number in cars:
            cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")

