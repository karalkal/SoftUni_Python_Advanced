# problem with this solution is (WAS) that it treats int input as strings
# therefore sorting at the end is wrong, i.e. "10" is before "2"
#  NOW IT IS SORTED (OUT) :-)
first_set = set([int(x) for x in input().split(" ")])
second_set = set([int(x) for x in input().split(" ")])
for times in range(int(input())):  # how many times
    user_entry = input().split()
    action, set_id_to_manipulate = user_entry[0], user_entry[1]

    if action == "Add":
        to_add = set([int(x) for x in user_entry[2:]])
        if set_id_to_manipulate == "First":
            first_set = first_set.union(to_add)
        elif set_id_to_manipulate == "Second":
            second_set = second_set.union(to_add)

    elif action == "Remove":
        to_remove = set([int(x) for x in user_entry[2:]])
        if set_id_to_manipulate == "First":
            first_set = first_set.difference(to_remove)
        elif set_id_to_manipulate == "Second":
            second_set = second_set.difference(to_remove)

    elif action == "Check":
        print(second_set.issubset(first_set) or second_set.issuperset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
