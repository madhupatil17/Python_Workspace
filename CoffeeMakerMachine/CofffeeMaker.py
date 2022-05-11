

def pull_report(resources_left):
    print(f"Resources available-")
    print(f"Water: {resources_left['water']}")
    print(f"Milk: {resources_left['milk']}")
    print(f"Coffee: {resources_left['coffee']}")
    print(f"Money: {resources_left['money']}")


def check_resources(coffee_type, menu, resources_left):
    order_ingredients = menu[coffee_type]['ingredients']

    for item in order_ingredients:
        if order_ingredients[item] > resources_left[item]:
            print(f"Sorry you request can not be processed. We don't have enough {item}.")
            return False
    return True


def update_resources(coffee_type, menu, resources_left):
    order_ingredients = menu[coffee_type]['ingredients']
    for item in order_ingredients:
        resources_left[item] -= order_ingredients[item]


def count_money():
    # money_received = take_money()
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    return round(total, 2)


def give_back_change(coffee_type, menu, total_money_received, resources_left):
    total_money_required = menu[coffee_type]['cost']
    resource_money = resources_left['money']

    if total_money_required < total_money_received:
        change_to_be_returned = total_money_received - total_money_required
        resources_left.update({'money': (total_money_required + resource_money)})
        print(f"Here's your ${round(change_to_be_returned, 2)} change in return")
        return True
    else:
        print("Sorry,that's not enough money. Money refunded.")
        return False


def process_money(coffee_type, menu, resources_left):
    money_received = count_money()
    if money_received > 0:
        print(f"Thank you for the payment of ${money_received}. We are processing your request...")
        if give_back_change(coffee_type, menu, money_received, resources_left):
            return True

    return False

