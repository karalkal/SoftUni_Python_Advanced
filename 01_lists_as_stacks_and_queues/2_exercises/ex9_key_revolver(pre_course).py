from collections import deque

single_bullet_price = int(input())
barrel_size = int(input())

bullets_as_list = [int(x) for x in input().split(" ")]
bullet_stack = deque(bullets_as_list)

locks_as_list = [int(x) for x in input().split(" ")]
locks_queue = deque(locks_as_list)

value_of_reward = int(input())
counter = 0
won = False

while True:
    this_shot = bullet_stack.pop()

    # either removes the lock or puts it back on the queue
    if this_shot <= locks_queue[0]:
        locks_queue.popleft()   # remove lock at zero position
        print("Bang!")
    else:                       # do nothing, just print
        print("Ping!")

    # count shots
    counter += 1
    if counter % barrel_size == 0 and counter < len(bullets_as_list):
        # compare to initial num of bullets, if out of bullets, cannot reload
        print("Reloading!")

    # won or lost
    if len(locks_queue) == 0:
        won = True
        break
    if len(bullet_stack) == 0:
        break

if not won:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    earned = value_of_reward - counter * single_bullet_price
    print(f"{len(bullet_stack)} bullets left. Earned ${earned}")
