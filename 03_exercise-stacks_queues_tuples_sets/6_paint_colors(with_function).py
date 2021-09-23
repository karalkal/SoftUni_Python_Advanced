from collections import deque


def check_secondary_colour(colours_so_far, composite_colour):
    if composite_colour == "orange" and ("red" not in colours_so_far or "yellow" not in colours_so_far):
        colours_so_far.remove("orange")
    elif composite_colour == "purple" and ("red" not in colours_so_far or "blue" not in colours_so_far):
        colours_so_far.remove("purple")
    elif composite_colour == "green" and ("blue" not in colours_so_far or "yellow" not in colours_so_far):
        colours_so_far.remove("green")
    return colours_so_far


primary = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
colour_deque = deque(input().split(" "))
found_colours = []

while len(colour_deque) > 1:  # if even number of entries, eventually it will pop last two and end
    front, back = colour_deque.popleft(), colour_deque.pop()

    if front + back in primary or front + back in secondary:
        found_colours.append(front + back)
    elif back + front in primary or back + front in secondary:
        found_colours.append((back + front))
    else:
        middle_index = len(colour_deque) // 2  # if even len - middle, if odd len - position before middle element
        # front_cut = front[:len(front) - 1]
        # back_cut = back[:len(back) - 1]
        front_cut = front[:- 1]
        back_cut = back[:- 1]
        if back_cut:
            colour_deque.insert(middle_index, back_cut)  # insert this one first, so that the next entry comes in front
        if front_cut:
            colour_deque.insert(middle_index, front_cut)

if colour_deque:  # if still has one element remaining
    remaining = colour_deque.pop()
    if remaining in primary or remaining in secondary:
        found_colours.append(remaining)

# now check secondary
for colour in found_colours:
    if colour in secondary:
        found_colours = check_secondary_colour(found_colours, colour)

print(found_colours)
