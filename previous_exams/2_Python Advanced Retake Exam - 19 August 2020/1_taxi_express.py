from collections import deque

customers_queue = deque([int(x) for x in input().split(", ")])
taxis_stack = deque([int(x) for x in input().split(", ")])
total_time = 0

while customers_queue and taxis_stack:
    if customers_queue[0] <= taxis_stack[-1]:  # Just peek
        add_time = customers_queue.popleft()
        total_time += add_time

    taxis_stack.pop()

if customers_queue:
    print("Not all customers were driven to their destinations")
    print("Customers left: ", end="")
    print(*customers_queue, sep=", ")

else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")


