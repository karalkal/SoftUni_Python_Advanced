rows, columns = [int(x) for x in input().split()]
matrix = []

best_list_ever = []
max_sum = - 88888888  # :-)
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows - 2):
    for c in range(columns - 2):
        current_sum = 0
        current_list = []
        r1 = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
        r2 = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
        r3 = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        current_sum = sum(r1) + sum(r2) + sum(r3)
        current_list.append(r1)
        current_list.append(r2)
        current_list.append(r3)
        if current_sum > max_sum:
            max_sum = current_sum
            best_list_ever = current_list

print(f"Sum = {max_sum}")
print(*best_list_ever[0])
print(*best_list_ever[1])
print(*best_list_ever[2])
