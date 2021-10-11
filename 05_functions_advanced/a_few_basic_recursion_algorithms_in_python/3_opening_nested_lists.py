def nested_list_to_flat(lists, flat_list=[]):
    for entry in lists:
        if isinstance(entry, list):
            nested_list_to_flat(entry)
        else:
            flat_list.append(entry)
    return flat_list


data = [1, 2, 3, 4, [51, 61, [722, 822, [9111, 1011, 1111, 1112]]]]
check_data = nested_list_to_flat(data)
print(check_data)
