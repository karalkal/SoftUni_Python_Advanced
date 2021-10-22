from collections import deque

males_stack = deque([int(x) for x in input().split()])
females_queue = deque([int(x) for x in input().split()])
matches_count = 0

while females_queue and males_stack:
    girl = females_queue.popleft()
    # we have a special case with e.g. -25, -50 etc...
    if girl <= 0:
        continue
    if girl % 25 == 0 and females_queue:  # check if we haven't already popped last item
        females_queue.popleft()
        continue

    boy = males_stack.pop()
    if boy <= 0:
        females_queue.appendleft(girl)
        continue
    if boy % 25 == 0 and males_stack:
        males_stack.pop()
        females_queue.appendleft(girl)
        continue

    # ... and finally we start matching
    if girl == boy:
        matches_count += 1
    else:
        males_stack.append(boy - 2)

print(f"Matches: {matches_count}")

if males_stack:
    males_stack.reverse()  # for some reason it's the other way round in the problem description output
    print("Males left: ", end="")
    print(*males_stack, sep=", ")
else:
    print("Males left: none")

if females_queue:
    print("Females left: ", end="")
    print(*females_queue, sep=", ")
else:
    print("Females left: none")
