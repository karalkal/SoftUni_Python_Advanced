def determine_new_position(r, c, command):
    if command == "up" and r > 0:
        return r - 1, c
    elif command == "down" and r + 1 < size:
        return r + 1, c
    elif command == "left" and c > 0:
        return r, c - 1
    elif command == "right" and c + 1 < size:
        return r, c + 1


def gifts_to_all(cur_row, cur_column, matrix, remaining_presents, nice_kids):
    if cur_row > 0 and (matrix[cur_row - 1][cur_column] == "V" or matrix[cur_row - 1][cur_column] == "X"):
        if matrix[cur_row - 1][cur_column] == "V":
            nice_kids -= 1
        matrix[cur_row - 1][cur_column] = "-"
        remaining_presents -= 1
    if cur_row < len(matrix) - 1 and (matrix[cur_row + 1][cur_column] == "V" or matrix[cur_row + 1][cur_column] == "X"):
        if matrix[cur_row + 1][cur_column] == "V":
            nice_kids -= 1
        matrix[cur_row + 1][cur_column] = "-"
        remaining_presents -= 1
    if cur_column > 0 and (matrix[cur_row][cur_column - 1] == "V" or matrix[cur_row][cur_column - 1] == "X"):
        if matrix[cur_row][cur_column - 1] == "V":
            nice_kids -= 1
        matrix[cur_row][cur_column - 1] = "-"
        remaining_presents -= 1
    if cur_column < len(matrix) - 1 and (
            matrix[cur_row][cur_column + 1] == "V" or matrix[cur_row][cur_column + 1] == "X"):
        if matrix[cur_row][cur_column + 1] == "V":
            nice_kids -= 1
        matrix[cur_row][cur_column + 1] = "-"
        remaining_presents -= 1
    return matrix, remaining_presents, nice_kids


remaining_presents = int(input())
ran_out_of_presents = False
size = int(input())
matrix = []
good_kids = 0

for r in range(size):
    matrix.append(input().split())
    for c in range(size):
        if matrix[r][c] == "S":
            position = (r, c)
        elif matrix[r][c] == "V":
            good_kids += 1
        # at the end only gifts given to good kids count
initial_good_kids = good_kids
while True:
    command = input()
    if command == "Christmas morning":
        break

    # guy moves away from position
    matrix[position[0]][position[1]] = "-"

    # determine new position depending on command
    position = determine_new_position(position[0], position[1], command)
    cur_row, cur_column = position

    # if finds good kid, just reduce count of available presents and change V to S (below)
    if matrix[cur_row][cur_column] == "V":
        remaining_presents -= 1
        good_kids -= 1

    # if finds cookies -> presents for all surrounding
    elif matrix[cur_row][cur_column] == "C":
        matrix, remaining_presents, good_kids = gifts_to_all(position[0], position[1], matrix, remaining_presents,
                                                             good_kids)
        neighbours = identify_neighbours(position[0], position[1], matrix)

    if remaining_presents <= 0:
        ran_out_of_presents = True
        matrix[cur_row][cur_column] = "S"  # put him in position for final shape of matrix
        break

    # Santa simply moves to the new position if not "C" (if "X" or "V" just deletes it)
    matrix[cur_row][cur_column] = "S"

if good_kids > 0 and ran_out_of_presents:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)

if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {initial_good_kids} happy nice kid/s.")
