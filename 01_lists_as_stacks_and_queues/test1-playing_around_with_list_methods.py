def test():
    b = "This is only a test"
    return b


items = ["ivan", "pesho", 44, 88.88, "kur"]
new = ["lajno", "gyz", "govno", 35.53]
items.append(new)

print(items)
print(items[-1][1][-1])
print(items[-1][-1:-4:-2])
print(1 == 1)
print(items[0][::-1])

print()
combined = items + new
print(combined)
combined[5].remove(35.53)
print(combined)
print(" / ".join(combined[5]))

print()
b = combined[5]
print(b)
a = " + ".join(combined.pop(5))
print(combined)
print(type(a))

print()
new_combined = combined + b
print(combined)
print(new_combined)

print()
print(list(reversed(combined)))
list_of_stringed_items = [str(x) for x in new_combined]
print(sorted(list_of_stringed_items, reverse=True))
print(sorted(list_of_stringed_items))
print(sorted(list_of_stringed_items)[1:3] + sorted(list_of_stringed_items, reverse=True)[-2:-4:-1])

print()
list_of_stringed_items.insert(0, test())
print(list_of_stringed_items)
print(*list_of_stringed_items, sep="\n")
print()
list_of_stringed_items.reverse()
print("\n".join(list_of_stringed_items))

print()
print("ivan" in list_of_stringed_items)
print(type(list_of_stringed_items))
print(("...").join(list_of_stringed_items))
print(*list_of_stringed_items, sep="...")
print(a is a)
z = a
print(a is z)
d, e = 8, 8
print(d is e)
f, g = [8], [8]
print(f is g)
k, l = "hello", "hello"
print(k is l)
m, n = "hell", "hello"
m += "o"
print(m, n, m is n)

print()
del list_of_stringed_items[:4]
print(list_of_stringed_items)

list_of_stringed_items[4:6] = []
print(list_of_stringed_items)
print()
list_of_stringed_items[-1] = (list_of_stringed_items[-1].split())
print(list_of_stringed_items)

list_of_stringed_items += list_of_stringed_items[-1]
print(list_of_stringed_items)


ff = "abcdefgh"
hh = list(ff)
print(hh)
