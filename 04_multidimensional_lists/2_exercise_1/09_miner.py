from collections import deque

size = int(input())
commands = deque(input().split())

matrix = []
for _ in range(size):
    matrix.append(input().split())

# find starting position and count coal
coal_available = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "s":
            current_position = (r, c)
        elif matrix[r][c] == "c":
            coal_available += 1

reached_end = False
while coal_available > 0 and not reached_end and commands:
    command = commands.popleft()
    if command == "left" and current_position[1] > 0:
        current_position = (current_position[0], current_position[1] - 1)
    elif command == "right" and current_position[1] < size - 1:
        current_position = (current_position[0], current_position[1] + 1)
    elif command == "up" and current_position[0] > 0:
        current_position = (current_position[0] - 1, current_position[1])
    elif command == "down" and current_position[0] < size - 1:
        current_position = (current_position[0] + 1, current_position[1])

    if matrix[current_position[0]][current_position[1]] == "c":
        matrix[current_position[0]][current_position[1]] = "*"
        coal_available -= 1
    if matrix[current_position[0]][current_position[1]] == "e":
        reached_end = True
if reached_end:
    print("Game over!", current_position)
else:
    if coal_available == 0:
        print("You collected all coal!", current_position)
    else:
        print(f"{coal_available} pieces of coal left.", current_position)
