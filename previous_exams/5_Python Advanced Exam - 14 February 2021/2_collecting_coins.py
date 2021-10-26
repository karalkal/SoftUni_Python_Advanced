def find_starting_position(matrix):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "P":
                return r, c


# in this solution if player returns to a position they have been to before, value will be 0 = > makes sanse but not required by Judge apparently

def move_left(row, column, coins, journey, matrix, kaput):
    if column == 0 or matrix[row][column - 1] == "X":
        coins = coins // 2
        kaput = True
    else:
        column -= 1
        coins += int(matrix[row][column])
        journey.append([row, column])
        matrix[row][column] = 0
    return row, column, coins, journey, matrix, kaput


def move_right(row, column, coins, journey, matrix, kaput):
    if column + 1 == size or matrix[row][column + 1] == "X":
        coins = coins // 2
        kaput = True
    else:
        column += 1
        coins += int(matrix[row][column])
        journey.append([row, column])
        matrix[row][column] = 0
    return row, column, coins, journey, matrix, kaput


def move_up(row, column, coins, journey, matrix, kaput):
    if row == 0 or matrix[row - 1][column] == "X":
        coins = coins // 2
        kaput = True
    else:
        row -= 1
        coins += int(matrix[row][column])
        journey.append([row, column])
        matrix[row][column] = 0
    return row, column, coins, journey, matrix, kaput


def move_down(row, column, coins, journey, matrix, kaput):
    if row + 1 == size or matrix[row + 1][column] == "X":
        coins = coins // 2
        kaput = True
    else:
        row += 1
        coins += int(matrix[row][column])
        journey.append([row, column])
        matrix[row][column] = 0
    return row, column, coins, journey, matrix, kaput


size = int(input())
# build matrix
matrix = []
for r in range(size):
    matrix.append(input().split())

row_current, column_current = find_starting_position(matrix)
# we don't need to see the location of the man, therefore we clear the value to avgoid errors:
matrix[row_current][column_current] = 0
coins = 0
journey = []
kaput, has_won = False, False

while True:
    command = input()
    if command == "left":
        row_current, column_current, coins, journey, matrix, kaput = \
            move_left(row_current, column_current, coins, journey, matrix, kaput)
    elif command == "right":
        row_current, column_current, coins, journey, matrix, kaput = \
            move_right(row_current, column_current, coins, journey, matrix, kaput)
    elif command == "up":
        row_current, column_current, coins, journey, matrix, kaput = \
            move_up(row_current, column_current, coins, journey, matrix, kaput)
    elif command == "down":
        row_current, column_current, coins, journey, matrix, kaput = \
            move_down(row_current, column_current, coins, journey, matrix, kaput)

    if kaput:
        break
    if coins >= 100:
        has_won = True
        break
if has_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for entry in journey:
    print(entry)

