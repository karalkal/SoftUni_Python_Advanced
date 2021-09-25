rows = int(input())
original_list = []
for _ in range(rows):
    column = [int(x) for x in input().split(", ")]
    original_list.append(column)

evens_only = []
for column in original_list:
    column_with_evens = []
    for element in column:
        if element % 2 == 0:
            column_with_evens.append(element)
    evens_only.append(column_with_evens)
print(evens_only)
