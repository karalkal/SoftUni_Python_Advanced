from collections import deque

list_robots = input().split(";")
dict_robots = {}
original_value = {}
for r in list_robots:
    this_robot = r.split("-")
    dict_robots[this_robot[0]] = 0
    original_value[this_robot[0]] = int(this_robot[1])

start_time = input().split(":")
hours, minutes, seconds = int(start_time[0]), int(start_time[1]), int(start_time[2])

items_deq = deque()
get_input = True
removed_item = False
while True:
    item_added = input()
    if item_added == "End":
        break
    else:
        items_deq.append(item_added)

while len(items_deq) > 0:
    seconds += 1
    processed = items_deq.popleft()  # if items in queue, pop the oldest one
    for k, v in dict_robots.items():
        if v != 0:
            dict_robots[k] -= 1
    # below must be proper datetime module for converting secs to mins to hours
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours == 24:
        hours = 0

    for k, value in dict_robots.items():
        if value == 0:  # if any of values is zero (robot can accept order), print...
            print(f"{k} - {processed} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
            dict_robots[k] = original_value[k]  # ... zero is replaced, countdown starts again, popped item disappears
            removed_item = True
            break
        else:
            removed_item = False  # we need to reset that if previous item is removed, i.e. set to True
    if not removed_item:
        items_deq.append(processed)  # item is placed at end if no robot available


