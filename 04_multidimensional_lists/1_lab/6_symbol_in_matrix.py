side_size = int(input())

matrix = []
for r in range(side_size):
    entry_listed = list(input())  # string is transformed to list of chars
    column = []
    for c in range(side_size):
        column.append(entry_listed[c])
    matrix.append(column)
# print(matrix)

find_this = input()
found_it = False
for r in range(side_size):
    for c in range(side_size):
        current_char = matrix[r][c]
        if current_char == find_this:
            result = (r, c)
            found_it = True
            break
    if found_it:
        break
if not found_it:
    print(f"{find_this} does not occur in the matrix")
else:
    print(result)