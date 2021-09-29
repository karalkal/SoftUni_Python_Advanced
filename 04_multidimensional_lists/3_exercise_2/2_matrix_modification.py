size = int(input())
matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break

    row, column, value = int(command[1]), int(command[2]), int(command[3])
    check_entries = (matrix, row, column, size)
    if row < 0 or column < 0 or row > size - 1 or column > size - 1:
        print("Invalid coordinates")
        continue

    if command[0] == ("Add"):
        matrix[row][column] = matrix[row][column] + value

    if command[0] == ("Subtract"):
        matrix[row][column] = matrix[row][column] - value

for row in matrix:
    print(*row)
