from collections import deque


def best_list_pureness(*args):
    times_to_rotate = args[1]
    queue_inverted = deque(args[0])
    best_result, best_rotation = 0, 0

    for r in range(times_to_rotate + 1):
        current_result = 0

        for i in range(len(queue_inverted)):
            current_result += queue_inverted[i] * i
        if current_result > best_result:
            best_result = current_result
            best_rotation = r

        number = queue_inverted.pop()
        queue_inverted.appendleft(number)
    return f"Best pureness {best_result} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
