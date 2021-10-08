from collections import deque


def fill_the_box(h, l, w, *args):
    volume = h * l * w
    queue = deque(args)
    for i in range(len(queue)):
        entry = queue.popleft()
        if entry == "Finish":
            break
        # else
        volume -= entry
        if volume <= 0:  # if overfilled...
            queue.append(0 - volume)  # ... we return the excess back to the queue
            return f"No more free space! You have {sum([x for x in queue if x != 'Finish'])} more cubes."
    return f"There is free space in the box. You could put {volume} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
