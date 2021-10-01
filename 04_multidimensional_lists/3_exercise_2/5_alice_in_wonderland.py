size = int(input())
maze = []
for r in range(size):
    maze.append(input().split())  # create the matrix
    for c in range(size):
        if maze[r][c] == "A":
            current_position = [r, c]  # find the location of Alice

collected = 0
has_failed = False
while True:
    command = input()
    y, x = current_position
    maze[y][x] = "*"  # Alice steps away from current position

    if command == "up":
        current_position = [y - 1, x]  # moves to new position [UP]
        y, x = current_position
        if y >= 0 and maze[y][x] != "R":  # if still in the game
            if maze[y][x].isdecimal():  # and finds number
                collected += int(maze[y][x])  # collects tea
            else:  # otherwise just continues
                continue
        else:
            if y >= 0 and maze[y][x] == "R":
                maze[y][x] = "*"
            has_failed = True
            break

    elif command == "down":
        current_position = [y + 1, x]  # moves to new position [DOWN]
        y, x = current_position
        if y < size and maze[y][x] != "R":  # if still in the game
            if maze[y][x].isdecimal():
                collected += int(maze[y][x])  # and collects tea
            else:
                continue
        else:
            if y < size and maze[y][x] == "R":
                maze[y][x] = "*"
            has_failed = True
            break

    elif command == "left":
        current_position = [y, x - 1]  # moves to new position [LEFT]
        y, x = current_position
        if x >= 0 and maze[y][x] != "R":  # if still in the game
            if maze[y][x].isdecimal():
                collected += int(maze[y][x])  # and collects tea
            else:
                continue
        else:
            if x >= 0 and maze[y][x] == "R":
                maze[y][x] = "*"
            has_failed = True
            break

    elif command == "right":
        current_position = [y, x + 1]  # moves to new position [RIGHT]
        y, x = current_position
        if x < size and maze[y][x] != "R":  # if still in the game
            if maze[y][x].isdecimal():
                collected += int(maze[y][x])  # and collects tea
            else:
                continue
        else:
            if x < size and maze[y][x] == "R":
                maze[y][x] = "*"
            has_failed = True
            break

    if collected >= 10:
        maze[y][x] = "*"  # before exiting we still mark the last location
        break

if has_failed:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for row in maze:
    print(*row)
# print(collected)
