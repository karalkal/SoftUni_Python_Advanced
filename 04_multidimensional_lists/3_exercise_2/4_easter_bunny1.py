size = int(input())
matrix = []
for _ in range(size):
    matrix.append(input().split())

best_result, best_route, best_direction = float('-inf'), [], ""

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "B":
            bunny_is_here = [r, c]

cur_row, cur_col = bunny_is_here
current_result, current_route = 0, []
# TRY UP
while cur_row > 0:
    cur_row -= 1
    if matrix[cur_row][cur_col] == "X":
        break
    current_result += int(matrix[cur_row][cur_col])
    current_route.append([cur_row, cur_col])
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "up"

cur_row, cur_col = bunny_is_here
current_result, current_route = 0, []
# TRY DOWN
while cur_row < size - 1:
    cur_row += 1
    if matrix[cur_row][cur_col] == "X":
        break
    current_result += int(matrix[cur_row][cur_col])
    current_route.append([cur_row, cur_col])
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "down"

cur_row, cur_col = bunny_is_here
current_result, current_route = 0, []
# TRY LEFT
while cur_col > 0:
    cur_col -= 1
    if matrix[cur_row][cur_col] == "X":
        break
    current_result += int(matrix[cur_row][cur_col])
    current_route.append([cur_row, cur_col])
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "left"

cur_row, cur_col = bunny_is_here
current_result, current_route = 0, []
# TRY RIGHT
while cur_col < size - 1:
    cur_col += 1
    if matrix[cur_row][cur_col] == "X":
        break
    current_result += int(matrix[cur_row][cur_col])
    current_route.append([cur_row, cur_col])
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "right"

print(best_direction)
for row in best_route:
    print(row)
print(best_result)
