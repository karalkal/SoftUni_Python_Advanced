from collections import deque

sequence_of_stops = deque()
number_of_stops = int(input())

for station in range(number_of_stops):
    this_entry = [int(x) for x in input().split()]  # first is petrol, second is distance

    fuel_minus_distance_to_next = this_entry[0] - this_entry[1]
    sequence_of_stops.append(fuel_minus_distance_to_next)
# print(sequence_of_stops)

# checking from each starting position...
for start_at in range(len(sequence_of_stops)):
    first_value = sequence_of_stops.popleft()
    current_fuel = first_value

    # ... if adding all values one by one till end will result in negative -> will not work
    # but if we have positive results everywhere -> we have a solution
    for remaining in sequence_of_stops:
        will_work_out = True

        if current_fuel < 0:  # we check starting station from above here, then adding every next to it
            will_work_out = False
            sequence_of_stops.append(first_value)  # if not going to work, we put it at the end of the queue
            break
        current_fuel += remaining  # this is where we add first to second, to third etc

    # if nested loop returns True, we have found a solution, hence:
    if will_work_out:
        print(start_at)
        break
