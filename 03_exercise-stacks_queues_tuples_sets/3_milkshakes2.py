from collections import deque

# had a solution where negative values are filtered out
# but we don't need to do that and here program will append negative values as well
portions_of_choc = deque([int(x) for x in input().split(", ")])
cups_of_milk = deque([int(x) for x in input().split(", ")])

good_shakes = 0
while good_shakes < 5 and cups_of_milk and portions_of_choc:
    '''If any of the values are equal to or below 0,
    you should remove them from the records before mixing it with the other ingredient. '''
    choc = portions_of_choc.pop()
    milk = cups_of_milk.popleft()
    if milk <= 0 and choc <= 0:
        continue
    if choc <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        portions_of_choc.append(choc)
        continue

    if choc == milk:  # remove both ingredients
        good_shakes += 1

    else:
        portions_of_choc.append(choc - 5)  # put at top of stack with value -5
        cups_of_milk.append(milk)  # put this cup of milk at end of queue

if good_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if portions_of_choc:
    print("Chocolate:", ", ".join(str(x) for x in portions_of_choc))
    # print("Chocolate: ", end="")
    # print(*portions_of_choc, sep=", ")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print("Milk:", ", ".join(str(x) for x in cups_of_milk))
    # print("Milk: ", end="")
    # print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")
