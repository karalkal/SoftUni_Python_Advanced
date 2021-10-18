def list_manipulator(*args):
    ll, command, location = args[0], args[1], args[2]


    if command == "add":
        values = [x for x in args[3:]]
        if location == "beginning":
            ll = values + ll
        elif location == "end":
            ll = ll + values

    elif command == "remove":
        to_remove = 1
        if len(args) > 3:
            to_remove = int(args[3])
        if location == "beginning":
            ll = ll[to_remove:]

        elif location == "end":
            ll = ll[:len(ll) - to_remove]

    return (ll)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
print()
print(list_manipulator([], "add", "end", 30, 40, 50))
print(list_manipulator([88], "add", "end", 30, 40, 50))
print(list_manipulator([], "add", "beginning", 30, 40, 50))
print(list_manipulator([88], "add", "beginning", 30, 40, 50))
print()
print(list_manipulator([1], "remove", "end"))
print(list_manipulator([1], "remove", "beginning"))
print(list_manipulator([1, 2, 3, 4], "remove", "beginning", 3))
print(list_manipulator([1, 2, 3, 4], "remove", "end", 3))
