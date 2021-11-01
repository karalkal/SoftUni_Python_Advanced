def shopping_list(budget, **kwargs):
    string_to_return = ""

    if budget < 100:
        string_to_return = "You do not have enough budget."

    else:
        items_in_basket = 0
        for item, price_quantity_tuple in kwargs.items():
            total_value = price_quantity_tuple[0] * price_quantity_tuple[1]
            if total_value < budget:
                budget -= total_value
                items_in_basket += 1
                string_to_return += f"You bought {item} for {total_value:.2f} leva.\n"
            if items_in_basket == 5:
                break

    return string_to_return


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
