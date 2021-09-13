go = {1: (11, 888), 4: (22, 444), 2: (44, 222), 8: (88, 111)}
print(go[1][1])

sorted_g = dict(sorted(go.items(), key=lambda x: x[1][1]))
print(sorted_g)

for x in go.items():
    print(f"{x[0]} is key, values are {x[1][0]} and {x[1][1]}")