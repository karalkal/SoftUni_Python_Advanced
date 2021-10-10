def age_assignment(*args, **kwargs):
    new_dict = {}
    # print(args, kwargs)
    for name in args:
        first_letter = name[0]
        new_dict[name] = kwargs[first_letter]  # get the value from original dict by its key and assign it to new dict
    return new_dict



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
