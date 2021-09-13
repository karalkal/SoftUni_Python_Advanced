# Write a program which reads an input consisting of a name and adds it to a queue until "End" is received.
# If you receive "Paid", print every customer's name, and empty the queue.
# Otherwise, you will receive a client and you should add them to the queue.
# When you receive "End", you must print the count of the remaining people in the queue in the format: "{count} people remaining.".
from collections import deque

customers_queue = deque()

while True:
    command = input()
    if command == "End":
        break

    elif command != "Paid":
        customers_queue.append(command)

    else:  # if command == "Paid"
        for c in range(len(customers_queue)):
            print(customers_queue.popleft())

print(f"{len(customers_queue)} people remaining.")
