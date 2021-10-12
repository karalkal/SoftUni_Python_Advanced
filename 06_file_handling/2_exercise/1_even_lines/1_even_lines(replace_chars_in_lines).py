import os

# Create new file each time ("w" mode)
file = open("1_test_a.txt", mode="w")
file.writelines("-I was quick to judge him, but it wasn't his fault.\n"
                "-Is this some kind of joke?! Is it?\n"
                "-Quick, hide here. It is safer.")
file.close()


to_replace = ["-", ",", ".", "!", "?"]
with open("1_test_a.txt", mode="r") as file:
    lines = file.readlines()
result = ""
for l in range(0, len(lines), 2):
    line = lines[l]
    list_original_sentence = line.split()
    list_result = []
    for word in list_original_sentence:
        unfiltered, filtered = [], []
        unfiltered = list(word)
        filtered = ["@" if char in to_replace else char for char in unfiltered]
        list_result.append(filtered)
    result = list_result[::-1]
    for word in result:
        print(*word, sep="", end=" ")
    print()
