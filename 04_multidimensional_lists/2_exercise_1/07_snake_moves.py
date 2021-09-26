from collections import deque

rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append(list(columns * "#"))

word_as_queue = deque(list(input()))

for r in range(rows):
    if r % 2 == 0:  # even rows
        for c in range(columns):
            cur_char = word_as_queue.popleft()
            word_as_queue.append(cur_char)
            matrix[r][c] = cur_char
    else:  # odd rows
        for c in range(columns - 1, -1, -1):
            cur_char = word_as_queue.popleft()
            word_as_queue.append(cur_char)
            matrix[r][c] = cur_char

for row in matrix:
    print(*row, sep="")
