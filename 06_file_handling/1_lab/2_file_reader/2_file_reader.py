with open("numbers.txt", mode="w") as file:
    nums = ["1", "2", "3", "4", "5"]
    for num in nums:
        file.write(num)
        file.write("\n")

with open("numbers.txt", mode="r") as file:
    total = 0
    for ch in file.read():
        if ch.isdigit():
            total += int(ch)
print(total)