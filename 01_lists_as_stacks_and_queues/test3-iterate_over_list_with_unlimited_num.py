index = 0
for i in range(80):
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    k = int(input())

    index = index + k
    if index > len(l) - 1:
        index = index % len(l)

    print(l[index])