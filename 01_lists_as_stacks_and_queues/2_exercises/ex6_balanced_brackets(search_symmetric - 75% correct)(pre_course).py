from collections import deque

# the problem with this solution is that it will not detect a case like
# (){{[()])) which is entirely valid
sequence = deque(input())

valid = True
for i in range(len(sequence) // 2):
    v1 = sequence.popleft()
    v2 = sequence.pop()
    if not ((v1 == "{" and v2 == "}") or \
            (v1 == "[" and v2 == "]") or \
            (v1 == "(" and v2 == ")")):
        valid = False
        print("NO")
        break

    if len(sequence) > 0:
        next_ch = sequence[0]
    else:
        next_ch = "whatever"

    if (v1 == "{" and ((next_ch != "[") and next_ch != "{")) or \
        (v1 == "[" and ((next_ch != "[") and next_ch != "(")) or \
        (v1 == "{" and ((next_ch != "[") and next_ch != "{")) or \
        (v1 == "(" and ((next_ch != "(") and v2 != ")")):
        valid = False
        print("NO")
        break

if valid:
    print("YES")