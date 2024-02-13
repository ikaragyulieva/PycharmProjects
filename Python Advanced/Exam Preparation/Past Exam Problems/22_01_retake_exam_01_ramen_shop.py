# You will be given two sequences of integers representing bowls of ramen and customers.
# Your task is to find out if you can serve all the customers.
# Start by taking the last bowl of ramen and the first customer.
# Try to serve every customer with ramen until we have no more ramen or customers left:
# •	Each time the value of the ramen is equal to the value of the customer,
# remove them both and continue with the next bowl of ramen and the next customer.
# •	Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with
# the value of that customer and remove the customer.
# Then try to match the same bowl of ramen (which has been decreased) with the next customer.
# •	Each time the customer's value is bigger than the value of the ramen bowl,
# decrease the value of the customer with the value of the ramen bowl and remove the bowl.
# Then try to match the same customer (which has been decreased) with the next bowl of ramen.
# Look at the examples provided for a better understanding of the problem.
# Input
# •	On the first line, you will receive integers representing the bowls of ramen,
# separated by a single space and a comma ", ".
# •	On the second line, you will receive integers representing the customers,
# separated by a single space and a comma ", ".
# Output
# •	If all customers are served, print: "Great job! You served all the customers."
# o	Print all left ramen bowls (if any) separated by comma and space in the format:
# "Bowls of ramen left: {bowls of ramen left}"
# •	Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
# o	Print all customers left separated by comma and space in the format "Customers left: {customers left}"

from collections import deque

ramen_bowls = [int(el) for el in input().split(', ')]
customers = deque(int(el) for el in input().split(', '))

while ramen_bowls and customers:
    current_bowl = ramen_bowls[-1]
    current_customer = customers[0]
    if current_bowl == current_customer:
        customers.popleft()
        ramen_bowls.pop()
    elif current_bowl > current_customer:
        ramen_bowls[-1] -= current_customer
        customers.popleft()
    elif current_customer > current_bowl:
        customers[0] -= current_bowl
        ramen_bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")


# --- Tests: ---
# Test1:
# 14, 25, 37, 43, 19
# 58, 23, 37
#
# Test2:
# 30, 13, 45
# 70, 25, 55, 15
#
# Test3:
# 30, 25
# 20, 35
#
# --- Outputs: ---
#
# Test1:
# Great job! You served all the customers
# Bowls of ramen left: 14, 6
#
# Test2:
# Out of ramen! You didn't manage to serve all customers.
# Customers left: 7, 55, 15
#
# Test3:
# Great job! You served all the customers.
