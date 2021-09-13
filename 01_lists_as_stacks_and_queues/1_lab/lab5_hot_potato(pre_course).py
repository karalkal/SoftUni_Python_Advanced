from collections import deque

kids = deque(input().split())
remove_this = int(input()) - 1

while len(kids) > 1:
    for c in range(remove_this):
        passed = kids.popleft()  # not picked...
        kids.append(passed)  # ... and goes back to the queue

    removed = kids.popleft()
    print(f"Removed {removed}")

print(f"Last is {''.join(kids)}")
