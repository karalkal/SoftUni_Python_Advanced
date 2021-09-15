num = int(input())
unique_names = set()
for n in range(num):
    unique_names.add(input())
print("\n".join(unique_names))