# Create new file each time ("w" mode)
file = open("1_test_a.txt", mode="w")
file.writelines("-I was quick to judge him, but it wasn't his fault.\n"
                "-Is this some kind of joke?! Is it?\n"
                "-Quick, hide here. It is safer.")
file.close()


chars_to_replace = ["-", ",", ".", "!", "?"]
with open("1_test_a.txt", mode="r") as file:
    lines = file.readlines()
result = []
for l in range(0, len(lines), 2):
    this_line = lines[l]
    for char in chars_to_replace:
        if char in this_line:
            this_line = this_line.replace(char, "@")
    print(*this_line.split()[::-1], sep=" ")

