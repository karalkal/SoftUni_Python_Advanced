size_of_side = int(input())
matrix = []

for _ in range(size_of_side):
    matrix.append([int(x) for x in input().split(" ")])

primary_diagonal = []
secondary_diagonal = []
for pr in range(size_of_side):
    primary_diagonal.append(matrix[pr][pr])
    sec = (size_of_side - 1) - pr  # last index is len - 1, one next row we need the penultimate, etc.
    secondary_diagonal.append((matrix[pr][sec]))

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)


