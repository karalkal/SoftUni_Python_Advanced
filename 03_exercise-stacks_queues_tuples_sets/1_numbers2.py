# problem with this solution is (WAS) that it treats int input as strings
# therefore sorting at the end is wrong, i.e. "10" is before "2"
#  NOW IT IS SORTED (OUT) :-)
first_set = set([int(x) for x in input().split(" ")])
second_set = set([int(x) for x in input().split(" ")])
for times in range(int(input())):  # how many times
    user_entry = input().split()
    action, set_id_to_manipulate = user_entry[0], user_entry[1]

    if action == "Add":
        if set_id_to_manipulate == "First":
            for ch in user_entry:
                if ch.isdecimal():
                    first_set.add(int(ch))
        elif set_id_to_manipulate == "Second":
            for ch in user_entry:
                if ch.isdecimal():
                    second_set.add(int(ch))

    elif action == "Remove":
        if set_id_to_manipulate == "First":
            for ch in user_entry:
                if ch.isdecimal():
                    if int(ch) in first_set:
                        first_set.remove(int(ch))
        elif set_id_to_manipulate == "Second":
            for ch in user_entry:
                if ch.isdecimal():
                    if int(ch) in second_set:
                        second_set.remove(int(ch))

    elif action == "Check":
        if second_set.issubset(first_set) or second_set.issuperset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
