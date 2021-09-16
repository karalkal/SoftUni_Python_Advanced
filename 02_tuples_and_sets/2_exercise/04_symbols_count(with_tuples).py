text = input()
list_of_tuples = []  # first value will be char, second will be count

for i in range(len(text)):
    sym = text[i]
    found_it = False

    # if first entry
    if len(list_of_tuples) == 0:
        new_tuple = (sym, 1)

    else:  # check if in list => iterate over all values, pointless but this is a tuple exercise, innit?

        for i in range(len(list_of_tuples)):
            # check, check, check... if found, pop, increment, add to list again
            if sym == list_of_tuples[i][0]:
                current_tuple = list_of_tuples.pop(i)  # we pop it...
                current_value = current_tuple[1]  # ... get its current value...
                new_tuple = (sym, current_value + 1)  # ... create a new one with old value + 1
                found_it = True
                break

            #  but if not found...
        if not found_it:
            new_tuple = (sym, 1)

    list_of_tuples.append(new_tuple)

sorted_list = sorted(list_of_tuples, key=lambda x: x[0])
# print(sorted_list)
for entry in sorted_list:
    character, times = entry
    print(f"{character}: {times} time/s")
