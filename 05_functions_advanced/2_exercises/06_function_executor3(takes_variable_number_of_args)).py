from math import prod


def func_executor(*args):
    list_of_results = []
    for expression in args:
        function, arguments = expression[0], expression[1]
        list_of_results.append(function(*arguments) )
    return list_of_results

def sum_numbers(*args):
    return sum(args)

def multiply_numbers(*args):
    return prod(args)

print(func_executor((sum_numbers, (1, 2, 77, 888)), (multiply_numbers, (2, 4)), (multiply_numbers, (22, -4, 5))))
print(func_executor((sum_numbers, (0, 2)), (multiply_numbers, (25, 4))))
print(func_executor((multiply_numbers, (222, -4))))
print(func_executor((multiply_numbers, (-2, -4, 80))))
