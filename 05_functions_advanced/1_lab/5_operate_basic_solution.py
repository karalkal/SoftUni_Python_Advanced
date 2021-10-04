def operate(operator, *args):
    if operator == "+":
        result = 0
        for n in args:
            result += n

    if operator == "-":
        result = args[0] * 2
        for n in args:
            result -= n

    elif operator == "*":
        result = 1
        for n in args:
            result *= n

    elif operator == "/":
        result = args[0] * args[0]
        for n in args:
            result /= n

    return result



print(operate("+", 1, 2, 3))
print(operate("/", 8, 4, 2))
