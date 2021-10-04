from itertools import permutations

# Write a program that reads a single string and prints all possible combinations of the characters in that string.
input_as_list = list(input())
size = len(input_as_list)
# result = permutations(input_as_list, size)
# print(type(result))
results = list(permutations(input_as_list, size))
for result in results:
    print("".join(result))
    # print(*result, sep="")


