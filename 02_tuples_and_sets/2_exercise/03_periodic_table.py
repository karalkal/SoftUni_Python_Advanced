def add_to_set(user_input):
    elements = user_input.split(" ")
    for element in elements:
        # HAVE TO ASK which option is faster as set will only accept unique values anyway
        # if element not in unique_elements:
        #     unique_elements.add(element)
        unique_elements.add(element)
    return unique_elements


num_of_entries = int(input())
unique_elements = set()
for _ in range(num_of_entries):
    unique_elements = add_to_set(input())

for el in unique_elements:
    print(el)