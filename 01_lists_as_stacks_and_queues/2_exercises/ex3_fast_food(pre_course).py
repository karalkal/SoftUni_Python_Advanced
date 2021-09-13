from collections import deque

quantity = int(input())
orders_list = input().split()
orders_deq = deque(int(x) for x in orders_list)
food_available = True

print(max(orders_deq))

for order in range(len(orders_deq)):
    this_order = orders_deq.popleft()  # taking next order

    if this_order > quantity:  # this order is popped so we print it again but it's not on the deque
        print("Orders left:", this_order, *orders_deq, sep=" ")
        food_available = False
        break
    else:
        quantity -= this_order

if food_available:
    print("Orders complete")
