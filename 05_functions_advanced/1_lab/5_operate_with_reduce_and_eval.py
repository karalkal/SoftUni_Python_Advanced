from functools import reduce


def operate(operator, *args):
        result = reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


        return result


print(operate("+", 1, 2, 3))
print(operate("/", 8, 4, 2))
