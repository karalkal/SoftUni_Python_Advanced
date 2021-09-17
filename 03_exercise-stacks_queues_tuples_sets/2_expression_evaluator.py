from collections import deque
from math import floor


def perform_math_operation(queue, operator):
    if operator == "+":  # of course we can use sum, just trying to have some consistency with other cases
        result = 0
        for i in queue:
            result += i

    elif operator == "-":
        result = queue[0]
        for i in range(1, len(queue)):
            result -= queue[i]

    elif operator == "*":
        result = 1
        for j in queue:
            result *= j

    elif operator == "/":
        result = queue[0]
        for i in range(1, len(queue)):
            result = floor(result / queue[i])
            # convert to int in case of fractional result, i.e. bankers remainder or whatever it is called

    return result


expression = input().split()
current_queue = deque()
for ch in expression:
    if ch not in "+-*/":
        current_queue.append(int(ch))
    else:
        result_of_this_operation = perform_math_operation(current_queue, ch)  # ch will be the math operator
        current_queue.clear()
        current_queue.append(result_of_this_operation)

print(result_of_this_operation)  # the final result from function must be... well, the final result
