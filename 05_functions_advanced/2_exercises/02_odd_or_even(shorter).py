def get_result(command, numbers):
    even_sum, odd_sum, count = 0, 0, len(numbers)
    remainder = 0 if command == "Even" else 1
    return sum(filter(lambda x: x % 2 == remainder,numbers )) * count

command = input()
numbers = [int(x) for x in input().split()]

print(get_result(command, numbers))
