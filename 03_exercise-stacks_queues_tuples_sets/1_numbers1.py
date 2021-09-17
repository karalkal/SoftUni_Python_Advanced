def return_set_with_added_values(incoming_set, nums_to_add):
    for num in nums_to_add:
        incoming_set.add(num)
    return incoming_set


def return_set_with_removed_values(incoming_set, nums_to_remove):
    for num in nums_to_remove:
        if num in incoming_set:  # need to also check if number is present
            incoming_set.remove(num)
    return incoming_set


first_set = set([int(x) for x in input().split()])
second_set = set(int(x) for x in input().split())
no_of_entries = int(input())
for times in range(no_of_entries):  # how many times
    user_entry = input()

    if user_entry.startswith("Add"):
        split_command = user_entry.split()
        add_to_this_set = split_command[1]
        nums_to_add = [int(x) for x in split_command[2:]]

        if add_to_this_set == "First":
            first_set = return_set_with_added_values(first_set, nums_to_add)
        elif add_to_this_set == "Second":
            second_set = return_set_with_added_values(second_set, nums_to_add)

    elif user_entry.startswith("Remove"):
        split_command = user_entry.split()
        remove_from_this_set = split_command[1]
        nums_to_remove = [int(x) for x in split_command[2:]]

        if remove_from_this_set == "First":
            first_set = return_set_with_removed_values(first_set, nums_to_remove)
        elif remove_from_this_set == "Second":
            second_set = return_set_with_removed_values(second_set, nums_to_remove)

    elif user_entry == "Check Subset":
        if second_set.issubset(first_set) or second_set.issuperset(first_set):
            print(True)
        else:
            print(False)
print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
