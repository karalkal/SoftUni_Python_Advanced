rows, columns = [int(x) for x in input().split(", ")]

ll_row = []
total = 0
for r in range(rows):
    ll_column = [int(x) for x in input().split(", ")]
    total += sum(ll_column)
    ll_row.append(ll_column)
print(total)
print(ll_row)