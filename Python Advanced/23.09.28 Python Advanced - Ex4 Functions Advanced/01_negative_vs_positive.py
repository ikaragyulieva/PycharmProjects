# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.

def sum_num(*args):
    negatives_sum = 0
    positive_sum = 0
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negatives_sum += num
    # Solution with comprehension:
    # negatives_sum = sum([x for x in args if x < 0])
    # positive_sum = sum([x for x in args if x > 0])
    return negatives_sum, positive_sum


nums = [int(x) for x in input().split()]

print(sum_num(*nums)[0])
print(sum_num(*nums)[1])
if abs(sum_num(*nums)[0]) > sum_num(*nums)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

