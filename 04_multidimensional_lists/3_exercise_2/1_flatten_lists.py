big_list = input().split("|")
# for i in range(len(big_list) - 1, -1, -1):
#     print(*big_list[i], end=" ")
result = []
for i in range(len(big_list) - 1, -1, -1):
    result += [int(x) for x in big_list[i].split()]
print(*result)


