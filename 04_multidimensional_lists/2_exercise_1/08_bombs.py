def edit_matrix(matrix, shot, size):
    x, y = shot  # unpack shot coordinates
    shot_value = matrix[x][y]
    if shot_value <= 0:
        return matrix

    matrix[x][y] = 0  # 5
    # first column if alright
    if y > 0 and x > 0:
        if matrix [x - 1][y - 1] > 0:  # 1
            matrix[x - 1][y - 1] -= shot_value  # 1
    if y > 0:  # 2
        if matrix[x][y - 1] > 0:  # 4
            matrix[x][y - 1] -= shot_value  # 4
    if y > 0 and x < size - 1:
        if matrix[x + 1][y - 1] > 0:  # 7
            matrix[x + 1][y - 1] -= shot_value  # 7
    # second column
    if x > 0:
        if matrix[x - 1][y] > 0:  # 2
            matrix[x - 1][y] -= shot_value  # 2
    if x < size - 1:
        if matrix[x + 1][y] > 0:  # 8
            matrix[x + 1][y] -= shot_value  # 8
    # third column if alright
    if y < size - 1 and x > 0:
        if matrix[x - 1][y + 1] > 0:  # 3
            matrix[x - 1][y + 1] -= shot_value  # 3
    if y < size - 1:
        if matrix[x][y + 1] > 0:  # 6
            matrix[x][y + 1] -= shot_value  # 6
    if y < size - 1 and x < size - 1:
        if matrix[x + 1][y + 1] > 0:  # 9
            matrix[x + 1][y + 1] -= shot_value  # 9
    return matrix


square_side = int(input())
matrix = []
for _ in range(square_side):
    matrix.append([int(x) for x in input().split()])

all_shots = input().split()

for h in range(len(all_shots)):
    this_shot = tuple(int(x) for x in all_shots[h].split(","))  # tuple containing shot coordinates
    matrix = edit_matrix(matrix, this_shot, square_side)

alive_count = 0
total_sum = 0
for r in range(square_side):
    for c in range(square_side):
        if matrix[r][c] > 0:
            alive_count += 1
            total_sum += matrix[r][c]
print(f"Alive cells: {alive_count}")
print(f"Sum: {total_sum}")

for row in matrix:
    print(*row)
