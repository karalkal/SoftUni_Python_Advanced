from collections import deque


def check_secondary_colour(colours_so_far, composite_colour):
    if composite_colour == "orange" and "red" in colours_so_far and "yellow" in colours_so_far:
        colours_so_far.append("orange")
    elif composite_colour == "purple" and "red" in colours_so_far and "blue" in colours_so_far:
        colours_so_far.append("purple")
    elif composite_colour == "green" and "blue" in colours_so_far and "yellow" in colours_so_far:
        colours_so_far.append("green")
    return colours_so_far


primary = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
colour_deque = deque(input().split(" "))
found_colours = []

while len(colour_deque) > 1:
    front, back = colour_deque.popleft(), colour_deque.pop()

    if front + back in primary:
        found_colours.append(front + back)
    elif back + front in primary:
        found_colours.append((back + front))

    elif front + back in secondary:
        found_sec = front + back
        found_colours = check_secondary_colour(found_colours, found_sec)
    elif back + front in secondary:
        found_sec = back + front
        found_colours = check_secondary_colour(found_colours, found_sec)

    else:
        middle_index = len(colour_deque) // 2
        front = front[:len(front) - 1]
        back = back[:len(back) - 1]
        colour_deque.insert(middle_index, front + back)

if len(colour_deque) == 1:
    remaining = colour_deque[0]
    if remaining in primary:
        found_colours.append(remaining)
    elif remaining in secondary:
        found_colours = check_secondary_colour(found_colours, remaining)

print(found_colours)