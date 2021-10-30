def flights(*args):
    flights_dict = {}
    for entry in range(0, len(args), 2):
        if args[entry] != "Finish":
            destination = args[entry]
            if destination not in flights_dict.keys():
                flights_dict[destination] = 0  # if not in, initialize it
            flights_dict[destination] += int(args[entry + 1])
        else:
            break
    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
