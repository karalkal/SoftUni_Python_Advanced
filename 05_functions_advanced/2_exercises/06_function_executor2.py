def func_executor(*args):
    list_of_results = []
    for expression in args:
        function, arguments = expression[0], expression[1]
        list_of_results.append(function(*arguments) )
    return list_of_results

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)), (multiply_numbers, (22, -4))))
print(func_executor((sum_numbers, (0, 2)), (multiply_numbers, (25, 4))))
print(func_executor((multiply_numbers, (222, -4))))
print(func_executor((multiply_numbers, (-2, -4))))
