def create_expressions(numbers, result = 0, expression = "", all_expressions = []):
    if not numbers:
        full_expression = f"{expression}={result}"
        # print(full_expression)
        all_expressions.append(full_expression)
        return
    create_expressions(numbers[1:], result + numbers[0], f"{expression}+{numbers[0]}")
    create_expressions(numbers[1:], result - numbers[0], f"{expression}-{numbers[0]}")
    return all_expressions

numbers_list = [int(x) for x in input().split(", ")]
print(*create_expressions(numbers_list), sep="\n")
