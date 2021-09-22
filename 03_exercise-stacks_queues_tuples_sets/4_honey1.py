from collections import deque

bees_queue = deque([int(x) for x in input().split()])
nectar_stack = deque([int(x) for x in input().split()])
operations_queue = deque(input().split())

collected_queue = deque()
total_honey = 0

while nectar_stack and bees_queue:
    bee = bees_queue[0]
    nectar = nectar_stack.pop()
    if bee <= nectar:
        bee = bees_queue.popleft()
        values_tuple = (bee, nectar)
        collected_queue.append(values_tuple)

while collected_queue:
    current_op = operations_queue.popleft()
    this_bee, its_load = collected_queue.popleft()

    if current_op == "+":
        total_honey += abs(this_bee + its_load)
    elif current_op == "-":
        total_honey += abs(this_bee - its_load)
    elif current_op == "*":
        total_honey += abs(this_bee * its_load)
    elif current_op == "/" and its_load != 0:
        total_honey += abs(this_bee / its_load)
print(f"Total honey made: {total_honey}")
if bees_queue:
    print("Bees left: ", end="")
    print(*bees_queue, sep=", ")
if nectar_stack:
    print("Nectar left: ", end="")
    print(*nectar_stack, sep=", ")
