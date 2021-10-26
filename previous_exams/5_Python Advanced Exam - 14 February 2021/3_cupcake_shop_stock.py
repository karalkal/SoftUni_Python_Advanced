def stock_availability(inventory_list, action, *args):
    if args:
        if action == "delivery":
            inventory_list += list(args)
        elif action == "sell":
            if isinstance(args[0], int):
                value = args[0]
                inventory_list = inventory_list[value:]
            else:
                for entry in args:
                    while entry in inventory_list:
                        inventory_list.remove(entry)
    else:
        if action == "sell":
            inventory_list = inventory_list[1:]

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
