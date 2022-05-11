from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
machine_on = True
while machine_on:
    choice = input(f"What would you like to have? ({menu.get_items()}). Type 'turn off' to turn the machine off. ")
    if choice == 'report':
        coffeeMachine.report()
        moneyMachine.report()
    elif choice == "turn off":
        machine_on = False
    else:
        order_item = menu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(order_item):
            moneyMachine.make_payment(order_item.cost)
            coffeeMachine.make_coffee(order_item)


