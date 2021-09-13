hoppa = [1, 2, 3, 4, 5, 6, 7, 8]
hoppa[2] = [22, 33, 44, 55]
print(hoppa)

hoppa[2:2] = [22, 33, 44, 55]
print(hoppa)

hoppa[6:7] = ["abhu"]
print(hoppa)

hoppa += hoppa
print(hoppa)

z = filter(lambda x: x == "abhu", hoppa)
print(list(z))