def determine_new_position(r, c, command):
    if command == "up" and r > 0:
        return r - 1, c
    elif command == "down" and r + 1 < size:
        return r + 1, c
    elif command == "left" and c > 0:
        return r, c - 1
    elif command == "right" and c + 1 < size:
        return r, c + 1


def identify_neighbours(r, c, matrix):
    neighbours = []
    if r > 0:
        neighbours.append([r - 1, c])
    if r < len(matrix):
        neighbours.append([r + 1, c])
    if c > 0:
        neighbours.append([r, c - 1])
    if c < len(matrix):
        neighbours.append([r, c + 1])
    return neighbours


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
        neighbours = identify_neighbours(position[0], position[1], matrix)

        for neighbour_row, neighbour_column in neighbours:
            if matrix[neighbour_row][neighbour_column] == "V":
                good_kids -= 1
                remaining_presents -= 1
            elif matrix[neighbour_row][neighbour_column] == "X":
                remaining_presents -= 1
            matrix[neighbour_row][neighbour_column] = "-"

    matrix[cur_row][cur_column] = "S"

    if remaining_presents <= 0:
        ran_out_of_presents = True
        matrix[cur_row][cur_column] = "S"  # put him in position for final shape of matrix
        break

    # Santa simply moves to the new position if not "C" (if "X" or "V" just deletes it)

if good_kids > 0 and ran_out_of_presents:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)

if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {initial_good_kids} happy nice kid/s.")
