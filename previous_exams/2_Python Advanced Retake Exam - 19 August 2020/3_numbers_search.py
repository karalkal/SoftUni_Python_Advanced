def numbers_searching(*args):
    result = []

    missing = None
    smallest, largest = min(args), max(args)
    for number in range(smallest + 1, largest):
        if number not in args:
            missing = number
    result.append(missing)

    duplicates = []
    for arg in args:
        if args.count(arg) > 1:
            duplicates.append(arg)
    result.append(sorted(set(duplicates)))

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
