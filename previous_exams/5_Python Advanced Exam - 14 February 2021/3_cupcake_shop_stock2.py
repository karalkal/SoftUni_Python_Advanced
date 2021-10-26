def stock_availability(inventory, action, *args):
    if action == "delivery":
        inventory += list(args)
    elif action == "sell":
        if not args:
            inventory = inventory[1:]
        else:
            if isinstance(args[0], int):
                inventory = inventory[args[0]:]
            else:
                for to_remove in args:
                    while to_remove in inventory:
                        inventory.remove(to_remove)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
