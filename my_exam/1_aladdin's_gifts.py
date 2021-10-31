from collections import deque

materials_stack = deque([int(x) for x in input().split()])
magics_queue = deque([int(x) for x in input().split()])
sum_of_ingredients = 0
gemstone, sculpture, gold, diamond = 0, 0, 0, 0

while materials_stack and magics_queue:
    material = materials_stack.pop()
    magic = magics_queue.popleft()
    sum_of_ingredients = material + magic

    if sum_of_ingredients < 100:
        if sum_of_ingredients % 2 == 0:
            sum_of_ingredients = material * 2 + magic * 3
        else:
            sum_of_ingredients = material * 2 + magic * 2
    elif sum_of_ingredients > 499:
        sum_of_ingredients = material / 2 + magic / 2

    if 100 <= sum_of_ingredients <= 199:
        gemstone += 1
    elif 200 <= sum_of_ingredients <= 299:
        sculpture += 1
    elif 300 <= sum_of_ingredients <= 399:
        gold += 1
    elif 400 <= sum_of_ingredients <= 499:
        diamond += 1

if (gemstone > 0 and sculpture > 0) or (gold > 0 and diamond > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_stack:
    print(f"Materials left: {', '.join(map(str, materials_stack))}")
if magics_queue:
    print(f"Magic left: {', '.join(map(str, magics_queue))}")

if diamond:
    print(f"Diamond Jewellery: {diamond}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if sculpture:
    print(f"Porcelain Sculpture: {sculpture}")
