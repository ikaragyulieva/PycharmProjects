# data = input().split(", ")
#
# rows = int(data[0])
# col = int(data[1])
#
# matrix = []
#
# for _ in range(rows):
#     elements = [int(el) for el in input().split(", ")]
#     matrix.append(elements)
#
# sum_nums = 0
#
# for row_index in range(rows):
#     for col_index in range(col):
#         sum_nums += matrix[row_index][col_index]
#
# print(sum_nums)
# print(matrix)

# Optimised solution:
data = input().split(", ")

rows = int(data[0])
col = int(data[1])

matrix = []
sum_nums = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(", ")]
    sum_nums += sum(elements)
    matrix.append(elements)

sum_nums = 0

print(sum_nums)
print(matrix)

