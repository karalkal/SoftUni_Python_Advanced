sequence = [int(x) for x in input().split(", ")]
value_to_search = sequence[int(input())]

total_ops = 0
while True:
    current_number = min(sequence)
    if current_number <= value_to_search:
        position_to_remove = sequence.index(current_number)
        sequence.pop(position_to_remove)
        total_ops += current_number
    else:
        break

    if not sequence:
        break

print(total_ops)
