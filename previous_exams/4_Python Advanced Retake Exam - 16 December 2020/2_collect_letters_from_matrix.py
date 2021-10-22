def move_up(matrix, word, r, c):
    if r == 0:  # punishment
        word = word[:-1]
        return matrix, word, r, c
    else:
        if matrix[r - 1][c] != "-":
            word.append(matrix[r - 1][c])
        matrix[r][c] = "-"
        matrix[r - 1][c] = "P"
        return matrix, word, r - 1, c


def move_down(matrix, word, r, c):
    if r == size - 1:  # punishment
        word = word[:-1]
        return matrix, word, r, c
    else:
        if matrix[r + 1][c] != "-":
            word.append(matrix[r + 1][c])
        matrix[r][c] = "-"
        matrix[r + 1][c] = "P"
        return matrix, word, r + 1, c


def move_left(matrix, word, r, c):
    if c == 0:  # punishment
        word = word[:-1]
        return matrix, word, r, c
    else:
        if matrix[r][c - 1] != "-":
            word.append(matrix[r][c - 1])
        matrix[r][c] = "-"
        matrix[r][c - 1] = "P"
        return matrix, word, r, c - 1


def move_right(matrix, word, r, c):
    if c == size - 1:  # punishment
        word = word[:-1]
        return matrix, word, r, c
    else:
        if matrix[r][c + 1] != "-":
            word.append(matrix[r][c + 1])
        matrix[r][c] = "-"
        matrix[r][c + 1] = "P"
        return matrix, word, r, c + 1


word_as_list = list(input())
size = int(input())
matrix = []
# create matrix
for i in range(size):
    matrix.append(list(input()))
# find position
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "P":
            row_player, column_player = r, c
# receive commands
number_of_commands = int(input())
for i in range(number_of_commands):
    command = input()
    if command == "up":
        matrix, word_as_list, row_player, column_player = move_up(matrix, word_as_list, row_player, column_player)
    elif command == "down":
        matrix, word_as_list, row_player, column_player = move_down(matrix, word_as_list, row_player, column_player)
    elif command == "left":
        matrix, word_as_list, row_player, column_player = move_left(matrix, word_as_list, row_player, column_player)
    elif command == "right":
        matrix, word_as_list, row_player, column_player = move_right(matrix, word_as_list, row_player, column_player)

print(*word_as_list, sep="")
# print("".join(word_as_list))
for row in matrix:
    print(*row, sep="", end="\n")
