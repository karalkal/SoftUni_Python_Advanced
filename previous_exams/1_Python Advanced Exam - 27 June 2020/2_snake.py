def create_matrix(size, matrix=[]):
    for _ in range(size):
        matrix.append(list(input()))
    return matrix


def find_initial_positions(matrix):
    snake_pos, tunnel_positions = (), []
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "S":
                snake_pos = r, c
            elif matrix[r][c] == "B":
                entrance = r, c
                tunnel_positions.append(entrance)
    if len(tunnel_positions) == 0:
        tunnel_positions = [(-88, -88),
                            (-88, -88)]  # If no tunnels in matrix - mock values for tunnel entrances => no effect

    return snake_pos, tunnel_positions


# For Variant 2: First initiate move by substituting coordinates
# and then perform checks straight away, this is too complex
def snake_moves(matrix, food, direction, r, c, tunnel_entrances):
    t1_row, t1_col, t2_row, t2_col = \
        tunnel_entrances[0][0], tunnel_entrances[0][1], tunnel_entrances[1][0], tunnel_entrances[1][1]

    if direction == "up":  # if and elif check if snake has reached entrance to tunnel
        if r - 1 == t1_row and c == t1_col:
            matrix[t1_row][t1_col] = "."
            matrix[t2_row][t2_col] = "S"
            r, c = t2_row, t2_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        elif r - 1 == t2_row and c == t2_col:
            matrix[t2_row][t2_col] = "."
            matrix[t1_row][t1_col] = "S"
            r, c = t1_row, t1_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        else:
            if matrix[r - 1][c] == "*":
                food += 1
            matrix[r - 1][c] = "S"
            r -= 1

    elif direction == "down":
        if r + 1 == t1_row and c == t1_col:
            matrix[t1_row][t1_col] = "."
            matrix[t2_row][t2_col] = "S"
            r, c = t2_row, t2_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        elif r + 1 == t2_row and c == t2_col:
            matrix[t2_row][t2_col] = "."
            matrix[t1_row][t1_col] = "S"
            r, c = t1_row, t1_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        else:
            if matrix[r + 1][c] == "*":
                food += 1
            matrix[r + 1][c] = "S"
            r += 1

    elif direction == "left":
        if r == t1_row and c - 1 == t1_col:
            matrix[t1_row][t1_col] = "."
            matrix[t2_row][t2_col] = "S"
            r, c = t2_row, t2_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        elif r == t2_row and c - 1 == t2_col:
            matrix[t2_row][t2_col] = "."
            matrix[t1_row][t1_col] = "S"
            r, c = t1_row, t1_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        else:
            if matrix[r][c - 1] == "*":
                food += 1
            matrix[r][c - 1] = "S"
            c -= 1

    elif direction == "right":
        if r == t1_row and c + 1 == t1_col:
            matrix[t1_row][t1_col] = "."
            matrix[t2_row][t2_col] = "S"
            r, c = t2_row, t2_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        elif r == t2_row and c + 1 == t2_col:
            matrix[t2_row][t2_col] = "."
            matrix[t1_row][t1_col] = "S"
            r, c = t1_row, t1_col
            tunnel_entrances = [(-88, -88), (-88, -88)]  # entrances data disappears
        else:
            if matrix[r][c + 1] == "*":
                food += 1
            matrix[r][c + 1] = "S"
            c += 1

    return matrix, food, r, c, tunnel_entrances


size = int(input())
food_eaten = 0
snake_fed = False
matrix = create_matrix(size)
snake_coordinates, tunnel_entrances = find_initial_positions(matrix)
current_row, current_column = snake_coordinates[0], snake_coordinates[1]

while True:
    command = input()
    matrix[current_row][current_column] = "."  # Snake vacates position

    # If snake goes out, no more "S" on matrix
    if (command == "up" and current_row == 0) \
            or (command == "down" and current_row == size - 1) \
            or (command == "left" and current_column == 0) \
            or (command == "right" and current_column == size - 1):
        break

    # If none of the above snake moves to new position
    matrix, food_eaten, current_row, current_column, tunnel_entrances = \
        snake_moves(matrix, food_eaten, command, current_row, current_column, tunnel_entrances)
    if food_eaten == 10:
        snake_fed = True
        break

    # print(*matrix, sep="\n")
    # print()

if snake_fed:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_eaten}")
# print(*matrix, sep="\n")
for r in matrix:
    print(*r, sep="")
