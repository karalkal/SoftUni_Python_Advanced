rows, columns = [int(x) for x in input().split(", ")]
matrix = []
max_sum = 0
for r in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for r in range(rows - 1):
    # to avoid out of range error as we will add one row below to calculation
    current_sum = 0
    for c in range(columns - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            tuple1 = (matrix[r][c], matrix[r][c + 1])
            tuple2 = (matrix[r + 1][c], matrix[r + 1][c + 1])
print(*tuple1)
print(*tuple2)
print(max_sum)
