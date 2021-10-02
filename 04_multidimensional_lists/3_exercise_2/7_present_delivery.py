def determine_new_position(cur_row, cur_column, command):
    if command == "up" and cur_row > 0:
        cur_row -= 1
        position = (cur_row, cur_column)
    elif command == "down" and cur_row + 1 < size:
        cur_row += 1
        position = (cur_row, cur_column)
    elif command == "left" and cur_column > 0:
        cur_column -= 1
        position = (cur_row, cur_column)
    elif command == "right" and cur_column + 1 < size:
        cur_column += 1
        position = (cur_row, cur_column)
    return position


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

    # if finds cookies -> presents for all surrounding
    if matrix[cur_row][cur_column] == "C":
        matrix, remaining_presents, good_kids = gifts_to_all(position[0], position[1], matrix, remaining_presents,
                                                             good_kids)
        if remaining_presents <= 0:
            ran_out_of_presents = True
            matrix[cur_row][cur_column] = "S"  # put him in position for final shape of matrix
            break

    # if finds good kid, just reduce count of available presents and change V to S (below)
    elif matrix[cur_row][cur_column] == "V":
        remaining_presents -= 1
        good_kids -= 1
        if remaining_presents <= 0:
            ran_out_of_presents = True
            matrix[cur_row][cur_column] = "S"  # put him in position for final shape of matrix
            break

    # Santa simply moves to the new position if neither "C" nor "V" (if "X" just deletes it)
    matrix[cur_row][cur_column] = "S"
    # for row in matrix:
    #     print(*row)
    # print()

if good_kids > 0 and ran_out_of_presents:
    print("Santa ran out of presents!")
# a bit stupid to run the loop again just for printing the result
for row in matrix:
    print(*row)

if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {initial_good_kids} happy nice kid/s.")
