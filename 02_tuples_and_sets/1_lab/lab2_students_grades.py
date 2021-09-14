num_of_marks = int(input())

dd = {}
for _ in range(num_of_marks):
    name, mark = tuple(input().split())
    if name not in dd:
        dd[name] = []
    dd[name].append(float(mark))

for k, v in dd.items():
    print(f"{k} -> ", end="")
    for value in v:
        print(f"{value:.2f}", end=" ")
    print(f"(avg: {sum(v)/len(v):.2f})")

