from collections import deque

# this solution takes into account scenarios like  (){{[()]))
expression = input()
brackets_deq = deque()
matched_bracket = True
for i in range(len(expression)):
    if expression[i] in ["{", "[", "("]:
        brackets_deq.append(expression[i])
    elif expression[i] in ["}", "]", ")"]:
        if len(brackets_deq) == 0:  # if closing brackets but no opening -> error
            matched_bracket = False
            break
        elif expression[i] == "}":
            check_against = brackets_deq.pop()
            if check_against != "{":
                matched_bracket = False
                break
        elif expression[i] == "]":
            check_against = brackets_deq.pop()
            if check_against != "[":
                matched_bracket = False
                break
        elif expression[i] == ")":
            check_against = brackets_deq.pop()
            if check_against != "(":
                matched_bracket = False
                break

# print(brackets_deq)
if matched_bracket:
    print("YES")
else:
    print("NO")