from collections import deque

# had a solution where negative values are filtered out
# but we don't need to do that and here program will append negative values as well
portions_of_choc = deque([int(x) for x in input().split(", ")])
cups_of_milk = deque([int(x) for x in input().split(", ")])

good_shakes = 0
got_it_baby = False
while not got_it_baby and cups_of_milk and portions_of_choc:
    '''If any of the values are equal to or below 0,
    you should remove them from the records before mixing it with the other ingredient. '''
    choc = portions_of_choc.pop()
    if choc <= 0:
        continue
    milk = cups_of_milk.popleft()
    if milk <= 0:
        portions_of_choc.append(choc)  # we append choc value again, so we can get it again at next iteration
        continue
    # if any of the values is negative, it is removed from its deque, the other one is not affected

    if choc == milk:  # remove both ingredients
        good_shakes += 1
        if good_shakes == 5:
            got_it_baby = True
            break
    else:
        portions_of_choc.append(choc - 5)  # put at top of stack with value -5
        cups_of_milk.append(milk)  # put this cup of milk at end of queue

if got_it_baby:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if portions_of_choc:
    print("Chocolate: ", end="")
    print(*portions_of_choc, sep=", ")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print("Milk: ", end="")
    print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")
