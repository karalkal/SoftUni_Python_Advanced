def set_up_board(board=[]):
    for c in range(8):
        board.append(input().split())
    return board


def determine_positions(board):
    queens_are_here = []
    for r in range(8):
        for c in range(8):
            if board[r][c] == "K":
                king_is_here = r, c
            elif board[r][c] == "Q":
                queens_are_here.append((r, c))
    return king_is_here, queens_are_here


def check_left(r, c):
    for current_col in range(c - 1, -1, -1):
        if board[r][current_col] == "Q":
            return False
        elif board[r][current_col] == "K":
            return True
    return False


def check_right(r, c):
    for current_col in range(c + 1, 8):
        if board[r][current_col] == "Q":
            return False
        elif board[r][current_col] == "K":
            return True
    return False


def check_up(r, c):
    for current_row in range(r - 1, -1, -1):
        if board[current_row][c] == "Q":
            return False
        elif board[current_row][c] == "K":
            return True
    return False


def check_down(r, c):
    for current_row in range(r + 1, 8):
        if board[current_row][c] == "Q":
            return False
        elif board[current_row][c] == "K":
            return True
    return False


def check_up_left(r, c):
    try:
        for _ in range(8):
            r -= 1
            c -= 1
            if r < 0 or c<0:
                break

            if board[r][c] == "Q":
                return False
            elif board[r][c] == "K":
                return True
    except IndexError:
        return False
    return False


def check_up_right(r, c):
    try:
        for _ in range(8):
            r -= 1
            c += 1
            if r < 0 or c > 7:
                break

            if board[r][c] == "Q":
                return False
            elif board[r][c] == "K":
                return True
    except IndexError:
        return False
    return False


def check_down_left(r, c):
    try:
        for _ in range(8):
            r += 1
            c -= 1
            if r > 7 or c < 0:
                break

            if board[r][c] == "Q":
                return False
            elif board[r][c] == "K":
                return True
    except IndexError:
        return False
    return False


def check_down_right(r, c):
    try:
        for _ in range(8):
            r += 1
            c += 1
            if r > 7 or c > 7:
                break

            if board[r][c] == "Q":
                return False
            elif board[r][c] == "K":
                return True
    except IndexError:
        return False
    return False


board = set_up_board()

king_location, queens_locations = determine_positions(board)

mating_queens = []
for queen_r, queen_c in queens_locations:

    if check_left(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_right(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_up(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_down(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])

    elif check_up_left(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_up_right(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_down_left(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])
    elif check_down_right(queen_r, queen_c):
        mating_queens.append([queen_r, queen_c])

if mating_queens:
    print(*mating_queens, sep="\n")
else:
    print("The king is safe!")
