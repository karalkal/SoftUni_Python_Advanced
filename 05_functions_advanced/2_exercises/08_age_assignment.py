def age_assignment(*args, **kwargs):
    new_dict = {}
    # print(args, kwargs)
    for key, value in kwargs.items():
        for name in args:
            if key == name[0]:
                new_dict[name] = value
    return new_dict



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
