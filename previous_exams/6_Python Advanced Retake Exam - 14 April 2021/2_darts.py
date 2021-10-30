def create_board():
    board = []
    for n in range(7):
        board.append(input().split())
    return board


def throw_dart(player_score, matrix, r, c):
    if 0 <= r < 7 and 0 <= c < 7:  # if different, i.e. outisde, will retuen value unchanged
        if matrix[r][c].isnumeric():
            player_score -= int(matrix[r][c])
        elif matrix[r][c] == "D":
            player_score -= \
                (int(matrix[0][c]) + int(matrix[6][c]) + \
                 int(matrix[r][0]) + int(matrix[r][6])) * 2
        elif matrix[r][c] == "T":
            player_score -= \
                (int(matrix[0][c]) + int(matrix[6][c]) + \
                 int(matrix[r][0]) + int(matrix[r][6])) * 3
        elif matrix[r][c] == "B":  # will definitely reduce it to below zero, e.g. wins
            player_score -= 501
    return player_score


name1, name2 = input().split(", ")
board = create_board()

player1 = {name1: 501}
player2 = {name2: 501}
winner = {}
attempt_no = 1
while True:
    row, column = eval(input())
    player1[name1] = throw_dart(player1[name1], board, row, column)
    if player1[name1] <= 0:
        winner = name1
        break

    row, column = eval(input())
    player2[name2] = throw_dart(player2[name2], board, row, column)
    if player2[name2] <= 0:
        winner = name2
        break

    attempt_no += 1

print(f"{winner} won the game with {attempt_no} throws!")
