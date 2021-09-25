num_of_lines = int(input())

matrix = []
for r in range(num_of_lines):
    column = []
    # Just want to make the process more obvious
    this_row = [int(x) for x in input().split()]  # First create list of ints from input...
    for c in range(num_of_lines):
        column.append(this_row[c])  # ... then add entries column by column to each row
    matrix.append(column)
# print(matrix)

sum_diagonal = 0
for i in range(num_of_lines):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)

