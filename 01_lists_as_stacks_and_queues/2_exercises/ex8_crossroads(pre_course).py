from collections import deque

green_duration = int(input())
reset_green = green_duration
amber_duration = int(input())
reset_amber = amber_duration

queue_of_cars_and_signals = deque()
current_queue = deque()
cars_passed = 0
crash = False

# Create queue of cars and "green" commands
while True:
    command = input()
    if command == "END":
        break
    else:
        queue_of_cars_and_signals.append(command)

while len(queue_of_cars_and_signals) > 0 and "green" in queue_of_cars_and_signals and crash == False:
    # while our queue is active, if there are any "green" remaining and if there is a crash
    green_active = False
    amber_active = False
    green_duration = reset_green

    # Create queue waiting for green
    while not green_active:
        cur_entry = queue_of_cars_and_signals.popleft()
        if cur_entry != "green":  # adding cars waiting for green light
            current_queue.append(cur_entry)
        else:
            green_active = True

    # GREEN LIGHT IS ON
    this_car = " "
    while green_active:
        if len(current_queue) == 0:
            green_active = False
            break
        # while cars are waiting for green signal
        trying_to_pass = current_queue.popleft()  # take first car from queue...
        this_car = deque(trying_to_pass)  # ... and transform to queue of characters

        while len(this_car) > 0:
            this_car.popleft()
            green_duration -= 1
            if green_duration == 0:
                amber_active = True
                green_active = False
                break
        if len(this_car) == 0:
            cars_passed += 1
            if green_active == 0:  # means that this car has passed and no other has started going while green
                amber_active = False

    if amber_active:
        if len(this_car) <= amber_duration:  # what remains from the car
            cars_passed += 1
            amber_active = False
        else:
            crash = True
            character_hit = this_car[amber_duration]
            # what remains minus duration of amber signal will pass, +1 is gonna be hit hard
            print(f"A crash happened!\n{trying_to_pass} was hit at {character_hit}.")
            break

if crash == False:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")