size = int(input())
matrix = []
for row in range(size):
    column = input().split()
    matrix.append(column)
    if "B" in column:
        bunny_is_here = [row, column.index("B")]
# The infinity condition was quite dodgy and unfair, fails if starting from zero,
# i.e. tests with negative numbers are carried out
best_result, best_direction, best_route = float('-inf'), "", []

current_result = 0
current_route = []
try_again = bunny_is_here
# LEFT
while bunny_is_here[1] > 0:
    bunny_is_here = [bunny_is_here[0], bunny_is_here[1] - 1]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "left"

current_result = 0
current_route = []
bunny_is_here = try_again
# RIGHT
while bunny_is_here[1] < size - 1:
    bunny_is_here = [bunny_is_here[0], bunny_is_here[1] + 1]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "right"

current_result = 0
current_route = []
bunny_is_here = try_again
# UP
while bunny_is_here[0] > 0:
    bunny_is_here = [bunny_is_here[0] - 1, bunny_is_here[1]]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "up"

current_result = 0
current_route = []
bunny_is_here = try_again
# DOWN
while bunny_is_here[0] < size - 1:
    bunny_is_here = [bunny_is_here[0] + 1, bunny_is_here[1]]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "down"

print(best_direction)
print(*best_route, sep="\n")
print(best_result)
