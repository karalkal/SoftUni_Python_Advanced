def get_magic_triangle(param):
    triangle = []
    row0 = [1]
    row1 = [1, 1]
    # first two rows will be always present by default, create them in advance
    triangle.append(row0)
    triangle.append(row1)

    for i in range(1, param - 1):  # 2 rows are already present -> reduce the required rows to be build
        this_row = [1]  # first entry in each new row is 1
        for j in range(i):  # will have 1 at each end, need to find only the middle values
            first = triangle[i][j]  # from previous row get nums one by one (first will be 1)
            second = triangle[i][j + 1]  # get next from previous row, will never be out of range because j+1 <= i
            this_row.append(first + second)  # add the required number, next iteration of j will get next pair of nums
        this_row.append(1)  # and add closing 1 to the row
        triangle.append(this_row)
    return triangle


get_magic_triangle(5)
get_magic_triangle(2)
get_magic_triangle(6)
get_magic_triangle(8)
get_magic_triangle(1)
