def add_cars(entry):
    parking_lot.append(entry)
    return parking_lot


def remove_cars(entry):
    parking_lot.remove(entry)
    return parking_lot


parking_lot = []
num_of_commands = int(input())
for n in range(num_of_commands):
    command = input().split(", ")
    if command[0] == "IN":
        parking_lot = add_cars(command[1])
    elif command[0] == "OUT":
        parking_lot = remove_cars(command[1])

parking_lot = set(parking_lot)
if len(parking_lot) == 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(parking_lot))


