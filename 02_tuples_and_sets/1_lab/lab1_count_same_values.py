def input_to_list(sequence):
    ll_str = sequence.split()
    ll = [float(x) for x in ll_str]
    return ll


def count_chars(our_list):
    dd = {}
    for ch in our_list:
        if ch not in dd:
            dd[ch] = 1
        else:
            dd[ch] += 1
    return dd


list_of_nums = input_to_list(input())
dict_of_occurrences = count_chars(list_of_nums)
for k, v in dict_of_occurrences.items():
    print(f"{k:.1f} - {v} times")
