# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
from collections import deque

expression = input()
stack_of_opening_brackets = deque()
for i in range(len(expression)):
    curr_char = expression[i]  # scan each character

    if curr_char == "(":  # if  front bracket found, record its index in stack
        stack_of_opening_brackets.append(i)

    elif curr_char == ")":  # if closing bracket found,
        cut_from = stack_of_opening_brackets.pop()  # pop index of last front
        cut_to = i + 1
        print(expression[cut_from:cut_to])


