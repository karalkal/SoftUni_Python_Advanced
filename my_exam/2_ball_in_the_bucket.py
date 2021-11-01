matrix = []
for _ in range(6):
    matrix.append(input().split())

points = 0
for attempt_no in range(3):
    row_hit, column_hit = eval(input())

    if row_hit < 0 or row_hit > 5 or \
            column_hit < 0 or column_hit > 5:
        continue

    if matrix[row_hit][column_hit] == "B":
        matrix[row_hit][column_hit] = "0"  # just to be consistent, other nums are strings too

        calculate_these = []
        for r in range(6):
            # There always will be exactly 6 buckets - 1 on each column
            # if matrix[r][column_hit].isdigit():
            #     points += int(matrix[r][column_hit])
            calculate_these.append(int(matrix[r][column_hit]))
        points += sum(calculate_these)
            # points += int(matrix[r][column_hit])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if 100 <= points <= 199:
        print(f"Good job! You scored {points} points, and you've won Football.")
    elif 200 <= points <= 299:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    elif points >= 300:
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
