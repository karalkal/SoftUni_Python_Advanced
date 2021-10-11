with open("text.txt", mode="w") as file:
    lines = [
        "This is some random line\n",
        "This is the second line\n",
        "And this is the third one",
    ]
    file.writelines(lines)
try:
    open("text.txt", mode="r")
    print('File found')
except:
    print('File not found')