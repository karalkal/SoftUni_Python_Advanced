def check_around(matrix, r, c):
    result = 0
    if r > 0 and c > 1:
        if matrix[r - 1][c - 2] == "K":  # 10 o'clock
            result += 1
    if r > 1 and c > 0:
        if matrix[r - 2][c - 1] == "K":  # 11 o'clock
            result += 1
    if r > 1 and c < size - 1:
        if matrix[r - 2][c + 1] == "K":  # 1 o'clock
            result += 1
    if r > 0 and c < size - 2:
        if matrix[r - 1][c + 2] == "K":  # 2 o'clock
            result += 1

    if r < size - 1 and c < size - 2:
        if matrix[r + 1][c + 2] == "K":  # 4 o'clock
            result += 1
    if r < size - 2 and c < size - 1:
        if matrix[r + 2][c + 1] == "K":  # 5 o'clock
            result += 1
    if r < size - 2 and c > 0:  # 7 o'clock
        if matrix[r + 2][c - 1] == "K":
            result += 1
    if r < size - 1 and c > 1:
        if matrix[r + 1][c - 2] == "K":  # 8 o'clock
            result += 1
    return result


size = int(input())
board = []
horses_count = 0

for i in range(size):
    current_row = list(input())
    # horses_count += current_row.count("K")  # count all horses
    board.append(current_row)

# for each horse we check how many other horses he is in conflict with
# i.e. hitting one another's positions
# the one involved in most conflicts needs to be removed
# once we have zero conflicts result, we stop

removed = 0
while True:
    conflicts = 0
    current_leader = ()  # here we will store coordinates of current leader
    # check each horse and remove the most "troublesome"
    # for _ in range(horses_count - 1):  # we should have at least one horse remaining... I guess
    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                checking_horse = [0, 0, 0]  # check for each one [y, x, conflicts]
                checking_horse[0], checking_horse[1] = r, c  # coordinates of THIS one
                checking_horse[2] = check_around(board, r, c)  # HIS conflicts
                if checking_horse[2] > conflicts:
                    conflicts = checking_horse[2]
                    current_leader = (checking_horse[0], checking_horse[1])
    #  at the end of this we should have the horse involved in most conflicts for this iteration
    if conflicts > 0:
        board[current_leader[0]][current_leader[1]] = "ХУЙ"
        removed += 1
    else:
        break
# print(board)
print(removed)
