def recalculate_matrix(matrix, row, column):
    # if mine is already planted there, do nothing, return matrix unamended
    if matrix[row][column] == "*":
        return matrix

    matrix[row][column] = "*"
    # up-left
    if row > 0 and column > 0:
        try:
            matrix[row - 1][column - 1] += 1
        except TypeError:
            pass
    # up
    if row > 0:
        try:
            matrix[row - 1][column] += 1
        except TypeError:
            pass
    # up-right
    if row > 0 and column < size - 1:
        try:
            matrix[row - 1][column + 1] += 1
        except TypeError:
            pass
    # right
    if column < size - 1:
        try:
            matrix[row][column + 1] += 1
        except TypeError:
            pass
    # down-right
    if row < size - 1 and column < size - 1:
        try:
            matrix[row + 1][column + 1] += 1
        except TypeError:
            pass
    # down
    if row < size - 1:
        try:
            matrix[row + 1][column] += 1
        except TypeError:
            pass
    # down-left
    if row < size - 1 and column > 0:
        try:
            matrix[row + 1][column - 1] += 1
        except(TypeError):
            pass
    # left
    if column > 0:
        try:
            matrix[row][column - 1] += 1
        except TypeError:
            pass

    return matrix


size = int(input())
matrix = []
for r in range(size):
    row = []
    for c in range(size):
        row.append(0)
    matrix.append(row)
# print(*matrix, sep="\n")

number_of_mines = int(input())
for m in range(number_of_mines):
    mine_coordinates = input().split(", ")
    row, column = int(mine_coordinates[0].lstrip("(")), int(mine_coordinates[1].rstrip(")"))

    matrix = recalculate_matrix(matrix, row, column)
for row in matrix:
    print(*row, sep=" ")
