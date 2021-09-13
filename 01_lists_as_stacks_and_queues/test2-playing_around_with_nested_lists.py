results_list = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8], [55, 56, 57, 58]]

for i in range(len(matrix[0])):
    single_item = []

    for item_num in matrix:
        single_item.append(item_num[i])

    results_list.append(single_item)

print(results_list)