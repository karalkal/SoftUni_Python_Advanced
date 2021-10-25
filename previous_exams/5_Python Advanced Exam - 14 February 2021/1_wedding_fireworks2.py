from collections import deque

effects_queue = deque([int(x) for x in input().split(", ") if int(x) > 0])
powers_stack = deque([int(x) for x in input().split(", ") if int(x) > 0])
fireworks_box = {"palm": 0, "willow": 0, "crosette": 0}
has_failed = False

while effects_queue and powers_stack and [x for x in fireworks_box.values() if x < 3]:
    effect = effects_queue.popleft()
    power = powers_stack.pop()
    mix = effect + power
    if mix % 15 == 0:
        fireworks_box["crosette"] += 1
    elif mix % 3 == 0:
        fireworks_box["palm"] += 1
    elif mix % 5 == 0:
        fireworks_box["willow"] += 1
    else:
        powers_stack.append(power)
        if effect > 1:
            effects_queue.append(effect - 1)  # if it's <= 0 we don't want it

for quantity in fireworks_box.values():
    if quantity < 3:
        message = "Sorry. You can't make the perfect firework show."
        has_failed = True
        break
    else:
        message = "Congrats! You made the perfect firework show!"
print(message)
if effects_queue:
    print(f"Firework Effects left: {', '.join(map(str, effects_queue))}")
if powers_stack:
    print(f"Explosive Power left: {', '.join(map(str, powers_stack))}")
print(f"Palm Fireworks: {fireworks_box['palm']}")
print(f"Willow Fireworks: {fireworks_box['willow']}")
print(f"Crossette Fireworks: {fireworks_box['crosette']}")
