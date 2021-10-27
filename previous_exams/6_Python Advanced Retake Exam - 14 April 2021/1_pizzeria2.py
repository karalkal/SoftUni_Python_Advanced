from collections import deque

pizzas_queue = deque([int(x) for x in input().split(", ") if 0 < int(x) <= 10])
chefs_stack = deque([int(x) for x in input().split(", ")])
pizzas_made = 0
while pizzas_queue and chefs_stack:
    pizza = pizzas_queue.popleft()
    chef = chefs_stack.pop()
    if pizza <= chef:
        pizzas_made += pizza
    else:
        pizzas_made += chef
        pizzas_queue.appendleft(pizza - chef)
if pizzas_queue:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizzas_queue))}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(map(str, chefs_stack))}")
