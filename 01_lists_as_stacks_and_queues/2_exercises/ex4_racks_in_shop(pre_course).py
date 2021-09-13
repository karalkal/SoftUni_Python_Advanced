from collections import deque

racks_count = 1
stack_of_items = deque(int(x) for x in input().split())
capacity = int(input())
new_rack = capacity
while len(stack_of_items) > 0:
    this_item = stack_of_items.pop()
    if this_item < new_rack:  # if item can fit -> deduct value
        new_rack -= this_item
    elif this_item == new_rack:  # if fits but no space remaining
        if len(stack_of_items) == 0:  # means it's the last item
            break
        else:  # new rack with full capacity
            new_rack = capacity
            racks_count += 1
    else:  # if doesn't fit, back to stack, get new rack with full capacity
        stack_of_items.append(this_item)
        racks_count += 1
        new_rack = capacity
print(racks_count)
