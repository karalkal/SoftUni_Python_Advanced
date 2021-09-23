from collections import deque


# def check_secondary_colour(colours_so_far, composite_colour):
#     if composite_colour == "orange" and ("red" not in colours_so_far or "yellow" not in colours_so_far):
#         colours_so_far.remove("orange")
#     elif composite_colour == "purple" and ("red" not in colours_so_far or "blue" not in colours_so_far):
#         colours_so_far.remove("purple")
#     elif composite_colour == "green" and ("blue" not in colours_so_far or "yellow" not in colours_so_far):
#         colours_so_far.remove("green")
#     return colours_so_far


primary = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]
colour_deque = deque(input().split(" "))
found_colours = []

while len(colour_deque) > 1:  # if even number of entries, eventually it will pop last two and end
    left, right = colour_deque.popleft(), colour_deque.pop()

    if left + right in primary or left + right in secondary:
        found_colours.append(left + right)
    elif right + left in primary or right + left in secondary:
        found_colours.append((right + left))
    else:
        middle_index = len(colour_deque) // 2  # if even len - middle, if odd len - position before middle element
        left = left[:len(left) - 1]
        right = right[:len(right) - 1]
        if right:
            colour_deque.insert(middle_index, right)  # insert this one first, so that the next entry comes in front
        if left:
            colour_deque.insert(middle_index, left)

if colour_deque:  # if still has one element remaining
    remaining = colour_deque.pop()
    if remaining in primary or remaining in secondary:
        found_colours.append(remaining)

# now check secondary
for colour in found_colours:
    if colour in secondary:
        # found_colours = check_secondary_colour(found_colours, colour)

        if colour == "orange" and ("red" not in found_colours or "yellow" not in found_colours):
            found_colours.remove("orange")
        elif colour == "purple" and ("red" not in found_colours or "blue" not in found_colours):
            found_colours.remove("purple")
        elif colour == "green" and ("blue" not in found_colours or "yellow" not in found_colours):
            found_colours.remove("green")

print(found_colours)
