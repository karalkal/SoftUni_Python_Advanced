def move_it_baby(matrix, cur_row, cur_column, direction, steps):
    if direction == "down":
        move_here = cur_row + steps
        if move_here < 5:
            if matrix[move_here][cur_column] == ".":
                cur_row += steps
    elif direction == "up":
        move_here = cur_row - steps
        if move_here >= 0:
            if matrix[move_here][cur_column] == ".":
                cur_row -= steps
    elif direction == "left":
        move_here = cur_column - steps
        if move_here >= 0:
            if matrix[cur_row][move_here] == ".":
                cur_column -= steps
    elif direction == "right":
        move_here = cur_column + steps
        if move_here < 5:
            if matrix[cur_row][move_here] == ".":
                cur_column += steps
    return cur_row, cur_column


def shot_or_not(matrix, cur_row, cur_column, direction, hit_targets):
    if direction == "right":
        # start checking from next box RIGHT to the end of row
        for c in range(cur_column + 1, 5):
            if matrix[cur_row][c] == "x":
                hit_targets.append([cur_row, c])  # this list is just for extra checks
                matrix[cur_row][c] = "."
                break
    if direction == "left":
        # start checking from next box LEFT to the start of row
        for c in range(cur_column - 1, -1, -1):
            if matrix[cur_row][c] == "x":
                hit_targets.append([cur_row, c])  # this list is just for extra checks
                matrix[cur_row][c] = "."
                break
    if direction == "up":
        # start checking from box ABOVE to the start of column
        for r in range(cur_row - 1, -1, -1):
            if matrix[r][cur_column] == "x":
                hit_targets.append([r, cur_column])  # this list is just for extra checks
                matrix[r][cur_column] = "."
                break
    if direction == "down":
        # start checking from box BELOW to the end of column
        for r in range(cur_row + 1, 5):
            if matrix[r][cur_column] == "x":
                hit_targets.append([r, cur_column])  # this list is just for extra checks
                matrix[r][cur_column] = "."
                break
    return matrix, hit_targets


matrix = []
initial_targets = []
shot_em_all = False

for r in range(5):
    matrix.append(input().split())
    for c in range(5):
        if matrix[r][c] == "A":
            current_row, current_column = r, c
            matrix[r][c] = "."  # just in case if we happen to pass through again
        if matrix[r][c] == "x":
            initial_targets.append([r, c])

number_of_commands = int(input())
hit_targets = []

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        direction, steps = command[1], int(command[2])
        current_row, current_column = move_it_baby(matrix, current_row, current_column, direction, steps)

    elif command[0] == "shoot":
        direction = command[1]
        matrix, hit_targets = shot_or_not(matrix, current_row, current_column, direction, hit_targets)
        if len(hit_targets) == len(initial_targets):
            shot_em_all = True
            break
if shot_em_all:
    print(f"Training completed! All {len(initial_targets)} targets hit.")
    print(*hit_targets, sep="\n")
else:
    print(f"Training not completed! {len(initial_targets) - len(hit_targets)} targets left.")
    print(*hit_targets, sep="\n")
