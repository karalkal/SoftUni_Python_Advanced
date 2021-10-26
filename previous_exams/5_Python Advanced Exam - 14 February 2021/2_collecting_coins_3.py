def build_matrix(size):
    matrix = []
    for r in range(size):
        matrix.append(input().split())
    return matrix


def find_initial_position():
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "P":
                return r, c


def check_next_step(r, c):
    if r < 0 or r >= len(matrix) or \
            c < 0 or c >= len(matrix) or \
            matrix[r][c] == "X":
        return False
    return True


matrix = build_matrix(int(input()))
coins = 0
route = []
is_alive = True
player_row, player_column = find_initial_position()
while True:
    direction = input()
    if direction == "up":
        player_row -= 1
    elif direction == "down":
        player_row += 1
    elif direction == "left":
        player_column -= 1
    elif direction == "right":
        player_column += 1
    if not check_next_step(player_row, player_column):
        is_alive = False
        break
    else:
        coins += int(matrix[player_row][player_column])
        route.append([player_row, player_column])
    if coins >= 100:
        break

if not is_alive:
    coins = int(coins / 2)
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
print(*route, sep="\n")
