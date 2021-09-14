num_of_names = int(input())

list_of_names = []
for n in range(num_of_names):
    list_of_names.append(input())

print(*set(list_of_names), sep="\n")