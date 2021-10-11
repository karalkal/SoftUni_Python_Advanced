# option 1
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# option 2
def factorial1(number1):
    if number1 < 2:  # same result as 1! = 1
        return 1
    return number1 * factorial1(number1 - 1)

# option 3
def factorial2(num):
    if num < 2:
        return 1
    num = num * factorial2(num - 1)
    print(num)
    return num


print(factorial(8))
print(factorial1(8))
print(factorial2(8))