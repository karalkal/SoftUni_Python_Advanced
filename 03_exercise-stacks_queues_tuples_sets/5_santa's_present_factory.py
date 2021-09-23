from collections import deque

doll = 0  # 150
train = 0  # 250
bear = 0  # 300
bicycle = 0  # 400
job_done = False

materials_stack = deque([int(x) for x in input().split()])
magic_queue = deque([int(x) for x in input().split()])

while materials_stack and magic_queue:
    material = materials_stack.pop()
    magic = magic_queue.popleft()
    product = material * magic

    # if matches given values
    if product == 150:
        doll += 1
    elif product == 250:
        train += 1
    elif product == 300:
        bear += 1
    elif product == 400:
        bicycle += 1
    # if negative
    elif product < 0:
        material += magic
        materials_stack.append(material)
    # if positive but doesn't match
    elif product > 0:
        material += 15
        materials_stack.append((material))
    # if zero, meaning one of values is zero
    elif product == 0:
        if material != 0:
            materials_stack.append(material)
        if magic != 0:
            magic_queue.appendleft(magic)

if (doll > 0 and train > 0) \
        or (bear > 0 and bicycle > 0):
    job_done = True

if job_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_stack:
    print("Materials left: ", end="")
    # print(*materials_stack, sep=", ")
    for m in range(len(materials_stack) - 1, 0, -1):
        print(materials_stack[m], end=", ")
    print(materials_stack[0])
if magic_queue:
    print("Magic left: ", end="")
    print(*magic_queue, sep=", ")

if bicycle:
    print("Bicycle:", bicycle)
if doll:
    print("Doll:", doll)
if bear:
    print("Teddy bear:", bear)
if train:
    print("Wooden train:", train)
