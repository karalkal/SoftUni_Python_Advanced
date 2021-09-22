from collections import deque


def perform_calculation(bee_and_nectar, operators):
    current_op = operators.popleft()
    this_bee, its_load = bee_and_nectar
    honey_to_add = 0
    if current_op == "+":
        honey_to_add = abs(this_bee + its_load)
    elif current_op == "-":
        honey_to_add = abs(this_bee - its_load)
    elif current_op == "*":
        honey_to_add = abs(this_bee * its_load)
    elif current_op == "/" and its_load != 0:
        honey_to_add = abs(this_bee / its_load)
        # honey_to_add = abs(int(this_bee / its_load))
    return honey_to_add


bees_queue = deque([int(x) for x in input().split()])
nectar_stack = deque([int(x) for x in input().split()])
operations_queue = deque(input().split())

total_honey = 0

while nectar_stack and bees_queue:
    bee = bees_queue[0]
    nectar = nectar_stack.pop()
    if bee <= nectar:
        bee = bees_queue.popleft()
        values_tuple = (bee, nectar)
        total_honey += perform_calculation(values_tuple, operations_queue)

print(f"Total honey made: {total_honey}")
if bees_queue:
    print("Bees left:", ", ".join(str(x) for x in bees_queue))
if nectar_stack:
    print("Nectar left:",  ", ".join(str(x) for x in nectar_stack))
