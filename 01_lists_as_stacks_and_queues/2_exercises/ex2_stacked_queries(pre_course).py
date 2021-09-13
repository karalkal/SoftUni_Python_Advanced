from collections import deque

sequence = deque()
count_of_commands = int(input())

for co_n in range(count_of_commands):
    command = input().split()  # split it because option "1" accepts value
    if command[0] == "1":
        sequence.append(int(command[1]))
    elif command[0] == "2" and len(sequence) > 0:
        sequence.pop()
    elif command[0] == "3" and len(sequence) > 0:
        print(max(sequence))
    elif command[0] == "4" and len(sequence) > 0:
        print(min(sequence))

# print(*sequence, sep=", ")
while len(sequence) > 1:
    print(sequence.pop(), end=", ")

if len(sequence) > 0:
    print(sequence.pop())


