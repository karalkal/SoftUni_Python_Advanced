num_of_invitations = int(input())
full_list = []

for g in range(num_of_invitations):
    full_list.append(input())

full_set = set(full_list)
while True:
    remove_or_end = input()
    if remove_or_end == "END":
        break
    full_set.remove(remove_or_end)

print(len(full_set))
print(*sorted(full_set), sep="\n")