text = input()
times = input()
try:
    print(text*int(times))
except ValueError:
    print("Variable times must be an integer")