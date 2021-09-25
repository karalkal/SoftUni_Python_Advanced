size_of_side = int(input())
matrix = []

for _ in range(size_of_side):
    matrix.append([int(x) for x in input().split(", ")])

primary_diagonal = []
secondary_diagonal = []
for pr in range(size_of_side):
    primary_diagonal.append(matrix[pr][pr])
    sec = (size_of_side - 1) - pr  # last index is len - 1, one next row we need the penultimate, etc.
    secondary_diagonal.append((matrix[pr][sec]))
# print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
# The next one looks better, if you ask me
print(f"Primary diagonal: ", end="")
print(*primary_diagonal, sep=", ", end="")
print(f". Sum: {sum(primary_diagonal)}")

print(f"Secondary diagonal: ", end="")
print(*secondary_diagonal, sep=", ", end="")
print(f". Sum: {sum(secondary_diagonal)}")



