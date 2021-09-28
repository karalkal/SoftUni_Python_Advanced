from collections import deque


def player_moves(player_position, command):
    if command == "L":
        new_position = player_position[0], player_position[1] - 1
    elif command == "R":
        new_position = player_position[0], player_position[1] + 1
    elif command == "U":
        new_position = player_position[0] - 1, player_position[1]
    elif command == "D":
        new_position = player_position[0] + 1, player_position[1]
    return new_position


def bunnies_grow(matrix):
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "B":
                # using small letters to avoid unlimited growth, will apitalize below
                if c > 0:
                    matrix[r][c - 1] = "b"
                if c < columns - 1:
                    matrix[r][c + 1] = "b"
                if r > 0:
                    matrix[r - 1][c] = "b"
                if r < rows - 1:
                    matrix[r + 1][c] = "b"
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "b":
                matrix[r][c] = "B"
    return matrix


rows, columns = [int(x) for x in input().split()]
matrix = []

for r in range(rows):
    matrix.append(list(input()))
    # determine initial position of player while here
    for c in range(columns):
        if matrix[r][c] == "P":
            player_position = (r, c)

commands = deque(list(input()))
won = False

while commands:
    # our man makes his move
    command = commands.popleft()
    prev_position = player_position  # record his previous position
    player_position = player_moves(player_position, command)

    matrix[prev_position[0]][prev_position[1]] = "."

    # with each iteration bunnies keep growing
    matrix = bunnies_grow(matrix)

    # if his position is out of the dimensions of the matrix -> WINS
    if player_position[0] < 0 or player_position[1] < 0 \
            or player_position[0] == rows or player_position[1] == columns:
        won = True
        break

    # guy is unlucky
    if matrix[player_position[0]][player_position[1]] == "B":
        break

        # in all other circumstances place him at the new location
        matrix[player_position[0]][player_position[1]] = "P"

for row in matrix:
    print(*row, sep="")
if won:
    print(f"won:", prev_position[0], prev_position[1])
else:
    print(f"dead:", player_position[0], player_position[1])
