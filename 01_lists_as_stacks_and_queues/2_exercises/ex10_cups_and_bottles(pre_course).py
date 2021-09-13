from collections import deque

cups_queue = deque(int(x) for x in input(). split())
bottles_stack = deque(int(x) for x in input(). split())
leftover = 0
enough_bottles = True

while len(cups_queue) > 0:  # while we have empty cups
    this_cup = cups_queue.popleft()
    while this_cup > 0:  # while this particular cup is empty
        new_bottle = bottles_stack.pop()
        this_cup -= new_bottle
        if this_cup < 0:
            leftover += abs(this_cup)
            break
    if len(bottles_stack) == 0:
        enough_bottles = False
        break

if enough_bottles:
    bottles_remaining = ""
    for b in range(len(bottles_stack)):
        bottles_remaining += str(bottles_stack.pop()) + " "
    print(f"Bottles: {bottles_remaining}")
    print(f"Wasted litters of water: {leftover}")
else:
    print("Cups:", *cups_queue)
    print(f"Wasted litters of water: {leftover}")

