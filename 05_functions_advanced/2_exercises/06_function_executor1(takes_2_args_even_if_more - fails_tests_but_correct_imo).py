'''
This solution fails most Judge tests with runtime error but this cannot be right.
The issue occurs when more than 2 arguments are passed to the sum and multiply functions.
This solution will disregard the excess ones while in the supposedly correct solution it must return an error.
'''

def func_executor(*args):
    list_of_results = []
    for expression in args:
        function, arguments = expression[0], expression[1]
        list_of_results.append(function(arguments[0], arguments[1]))
    return list_of_results

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)), (multiply_numbers, (22, -4))))
print(func_executor((sum_numbers, (0, 2)), (multiply_numbers, (25, 4))))
print(func_executor((multiply_numbers, (222, -4))))
print(func_executor((multiply_numbers, (-2, -4))))