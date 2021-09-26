rows, columns = [int(x) for x in input().split()]
result = []

for r in range(rows):
    this_row = []
    for c in range(columns):
        palindrome = chr(97 + r) + chr(97 + c + r) + chr(97 + r)  # second letter must be after 1st/3rd
        # print(palindrome)
        this_row.append(palindrome)
    result.append(this_row)

for box in result:
    print(*box)

