rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split()])
    # print(matrix)

for c in range(columns):
    sum_of_row = 0
    for r in range(rows):
        # print(matrix[r][c])
        sum_of_row += matrix[r][c]
    print(sum_of_row)
