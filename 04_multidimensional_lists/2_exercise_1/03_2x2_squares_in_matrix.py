rows, columns = [int(x) for x in input().split()]
matrix = []
found_occ = 0
for _ in range(rows):
    matrix.append(input().split())

for r in range(rows - 1):  # to avoid out of range error
    for c in range(columns - 1):
        one, two, three, four = matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]
        if one == two and one == three and one == four:
            found_occ += 1

# if not found_occ:
#     print("No 2x2 squares of equal cells exist.")
# else:
print(found_occ)
