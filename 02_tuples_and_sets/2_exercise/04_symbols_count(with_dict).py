text = input()
dict_of_chars = {}  # first value will be char, second will be count

for i in range(len(text)):
    sym = text[i]
    if sym not in dict_of_chars.keys():
        # we will add it with a value of 0
        dict_of_chars[sym] = 0
        # and add 1 to current num, regardless if it's zero
    dict_of_chars[sym] += 1

sorted_dict = dict(sorted(dict_of_chars.items(), key=lambda x: x[0]))
for char, times in sorted_dict.items():
    print(f"{char}: {times} time/s")
