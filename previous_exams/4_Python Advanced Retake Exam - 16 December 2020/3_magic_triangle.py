def get_magic_triangle(param):
    triangle = []
    row0 = [1]
    row1 = [1, 1]

    # row2 = [1, row1[0] + row1[1], 1]
    # row3 = [1, row2[0] + row2[1], row2[1] + row2[2],  1]
    # row4 = [1, row3[0] + row3[1], row3[1] + row3[2], row3[2] + row3[3], 1]
    # row5 = [1, row4[0] + row4[1], row4[1] + row4[2], row4[2] + row4[3], row4[3] + row4[4], 1]
    # print(row0, row1, row2, row3, row4, row5)
    # SOLVED THIS ENTIRELY ON MY OWN BUDDY!
    triangle.append(row0)
    triangle.append(row1)
    for i in range(1, param - 1):  # 2 rows are already built->we reduce the required rows to build
        this_row = [1]
        for j in range(i):  # wil have 1 at each end, need to find only the middle values
            first = triangle[i][j]
            second = triangle[i][j + 1]
            this_row.append(first + second)
        this_row.append(1)
        triangle.append(this_row)
    # print(triangle)
    return triangle


get_magic_triangle(5)
get_magic_triangle(2)
get_magic_triangle(6)
get_magic_triangle(8)
get_magic_triangle(1)
