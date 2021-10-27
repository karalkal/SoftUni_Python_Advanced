from collections import deque

pizzas_queue = deque([int(x) for x in input().split(", ") if 0 < int(x) <= 10])
employees = [int(x) for x in input().split(", ")]
count_pizzas = 0

while pizzas_queue and employees:
    this_order = pizzas_queue.popleft()
    this_employee = employees.pop()
    if this_employee >= this_order:
        count_pizzas += this_order
        continue
    else:  # order is larger than employee's capability
        remaining = this_order - this_employee
        count_pizzas += this_employee
        pizzas_queue.appendleft(remaining)

if not pizzas_queue:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {count_pizzas}")
    print(f"Employees: ", end = "")
    print(*employees, sep=", ")

else:
    print("Not all orders are completed.")
    print("Orders left: ", end="")
    print(*pizzas_queue, sep=", ")

