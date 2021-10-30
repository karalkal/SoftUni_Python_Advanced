def create_board():
    matrix = []
    for r in range(7):
        matrix.append(input().split())
    return matrix


def shot_result():
    shot_row, shot_column = [int(x) for x in input()[1:-1].split(", ")]
    return shot_row, shot_column


def calculate_score(player_score, r, c):
    if r < 0 or r >= 6 or c < 0 or c >= 6:
        return player_score
    # if invalid value, i.e. none of the below, it will still return player's current score
    if matrix[r][c].isdigit():
        player_score -= int(matrix[r][c])
    elif matrix[r][c] == "D":
        player_score -= 2 * (int(matrix[0][c]) + int(matrix[-1][c]) + int(matrix[r][0]) + int(matrix[r][-1]))
    elif matrix[r][c] == "T":
        player_score -= 3 * (int(matrix[0][c]) + int(matrix[-1][c]) + int(matrix[r][0]) + int(matrix[r][-1]))
    elif matrix[r][c] == "B":
        player_score -= 501
    return player_score


players = {player: 501 for player in input().split(", ")}
matrix = create_board()
attempts = 0
winner = None

while not winner:
    attempts += 1
    for current_player in players.keys():
        shot_row, shot_column = shot_result()
        players[current_player] = calculate_score(players[current_player], shot_row, shot_column)
        if players[current_player] <= 0:
            winner = current_player
            break
print(f"{winner} won the game with {attempts} throws!")
