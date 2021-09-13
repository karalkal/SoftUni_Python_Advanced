# Write program that: Reads an input string, Reverses it using a stack, Prints the result back on the console
from collections import deque

stack = deque(input())
result = ""
for i in range(len(stack)):
    result += stack.pop()

print(result)
