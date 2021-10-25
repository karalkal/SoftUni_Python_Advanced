from collections import deque

palm, willow, crossette = 0, 0, 0
effects_queue = deque([int(x) for x in input().split(", ")])
power_stack = deque([int(x) for x in input().split(", ")])
has_collected_all = False

while effects_queue and power_stack:
    effect = effects_queue.popleft()
    if effect <= 0:
        continue
    power = power_stack.pop()
    if power <= 0:
        effects_queue.appendleft(effect)
        continue


    if (effect + power) % 3 == 0 and (effect + power) % 5 != 0:
        palm += 1
    elif (effect + power) % 5 == 0 and (effect + power) % 3 != 0:
        willow += 1
    elif (effect + power) % 15 == 0:
        crossette += 1
    else:
        effects_queue.append(effect - 1)
        power_stack.append(power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        has_collected_all = True
        break

if has_collected_all:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects_queue:
    print("Firework Effects left: ", end="")
    print(*effects_queue, sep=", ")
if power_stack:
    print("Explosive Power left: ", end="")
    print(*power_stack, sep=", ")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
