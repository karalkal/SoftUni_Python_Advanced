num = int(input())
matrix = []
for _ in range(num):
    matrix.append([int(x) for x in input().split(", ")])
# print(matrix)

result = []
for row in matrix:
    for element in row:
        result.append(element)
print(result)
