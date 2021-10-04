from itertools import combinations

players = input().split(", ")
max_allowed = int(input())

result = list(combinations(players, max_allowed))
for combination in result:
    print(*combination, sep=", ")