def recursive_power(number, power):
    # result = 1
    # for i in range(power):
    #     result *= number
    # return result

    if power == 0:
        return 1
    else:
        return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
