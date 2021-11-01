def create_matrix():
    matrix = []
    for _ in range(6):
        matrix.append(input().split())
    return matrix


def evaluate_shot(entry):
    row, column = None, None
    split_entry = entry.split(", ")
    row = int(split_entry[0].lstrip("("))
    column = int(split_entry[1].rstrip(")"))
    return (row, column)


def is_valid_shot(row_hit, column_hit):
    if (row_hit < 0 or row_hit > 5 or \
        column_hit < 0 or column_hit > 5) or \
            matrix[row_hit][column_hit] != "B":
        return False
    return True


def calculate_column(column_hit):
    points_to_add = 0
    for r in range(6):
        points_to_add += int(matrix[r][column_hit])
    return points_to_add


def check_reward(points):
    prize_won = None
    if 100 <= points <= 199:
        prize_won = "Football"
    elif 200 <= points <= 299:
        prize_won = "Teddy Bear"
    elif points >= 300:
        prize_won = "Lego Construction Set"
    return prize_won


matrix = create_matrix()
points = 0
prize_won = None

for attempt_no in range(3):
    row_hit, column_hit = evaluate_shot(input())
    if not is_valid_shot(row_hit, column_hit):
        continue

    else:
        matrix[row_hit][column_hit] = "0"  # just to be consistent, other nums are strings too
        points += calculate_column(column_hit)

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    prize_won = check_reward(points)
    print(f"Good job! You scored {points} points, and you've won {prize_won}.")
