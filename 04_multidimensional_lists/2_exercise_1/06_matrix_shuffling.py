rows, columns = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())

error_message = "Invalid input!"
while True:
    command = input()
    if command == "END":
        break
    if not command.startswith("swap "):  # if swap (+space) not first word
        print(error_message)
        continue
    else:
        params = command.split()
        if not len(params) == 5:  # if contains more than 5 entries
            print(error_message)
            continue
        x1, y1, x2, y2 = int(params[1]), int(params[2]), int(params[3]), int(params[4])
        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:  # check for negative indexes
            print(error_message)
            continue
        if x1 > columns or x2 > columns or y1 > rows or y2 > rows:
            print(error_message)
            continue

        else:  # real action starts here
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            # print(matrix)
        for row in matrix:
            print(*row)
