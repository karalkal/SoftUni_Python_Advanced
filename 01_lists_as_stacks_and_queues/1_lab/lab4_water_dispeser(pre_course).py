# keeps track of people who are getting water from a dispenser and the amount of water left at the end.
from collections import deque

litres = int(input())
waiting_queue = deque()

# adding people to queue
while True:
    person = input()
    if person == "Start":
        break

    waiting_queue.append(person)

# start removing people from queue
while True:
    command = input()
    if command == "End":
        break

    # if other command given
    command = command.split()

    if command[0] == "End":
        break

    elif command[0] == "refill":
        litres += int(command[1])

    else:
        quantity_required = int(command[0])
        current = waiting_queue.popleft()

        if quantity_required > litres:
            print(f"{current} must wait")

        else:
            print(f"{current} got water")
            litres -= quantity_required

print(f"{litres} liters left")
