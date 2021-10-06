def get_result(command, numbers):
    even_sum, odd_sum, count = 0, 0, len(numbers)
    if command == "Even":
        for n in numbers:
            if n % 2 == 0:
                even_sum += n

        return even_sum * count
    else:
        for n in numbers:
            if n % 2 == 1:
                odd_sum += n
        return odd_sum * count

command = input()
numbers = [int(x) for x in input().split()]

result = get_result(command, numbers)
print(result)
