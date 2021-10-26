def create_matrix():
    for i in range(int(input())):
        matrix.append(input().split())
    return matrix


def find_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "P":
                return r, c


def snake_moves(direction, matrix):
    if direction == "up":
        return current_row - 1, current_column
    if direction == "down":
        return current_row + 1, current_column
    if direction == "left":
        return current_row, current_column - 1
    if direction == "right":
        return current_row, current_column + 1


def check_if_alive(r, c, matrix):
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix) \
            or matrix[r][c] == "X":
        return False
    return True


matrix = []
route = []
coins = 0
has_won = False

create_matrix()
current_row, current_column = find_position(matrix)
while True:
    direction = input()
    next_row, next_column = snake_moves(direction, matrix)

    if check_if_alive(next_row, next_column, matrix):
        current_row, current_column = next_row, next_column  # moves to new position
        coins += int(matrix[current_row][current_column])  # add relevant value
        route.append([current_row, current_column])
        matrix[current_row][current_column] = 0  # just in case, if player returns there shouldn't be a coin available
        if coins >= 100:
            has_won = True
            break
    else:  # has exited matrix or has hit X
        break

if has_won:
    print(f"You won! You've collected {coins} coins.")
else:
    coins = coins // 2
    print(f"Game over! You've collected {coins} coins.")
print("Your path: ")
print(*route, sep="\n")
