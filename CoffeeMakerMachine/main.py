from Resources import MENU, resources
from CoffeeMakerMachine import CofffeeMaker
machine = CofffeeMaker()

def start_machine():
    orders = True
    while orders:
        print()
        machine.pull_report(resources)
        requirement = input("What would you like to have? (Latte, Espresso, Cappuccino): ").lower()
        while requirement not in ['report', 'espresso', 'latte', 'cappuccino']:
            print("Please provide a valid input")
            requirement = input("What would you like to have? (Latte, Espresso, Cappuccino): ").lower()
        if requirement == "report":
            machine.pull_report(resources)
        else:
            if machine.check_resources(requirement, MENU, resources):
                if machine.process_money(requirement, MENU, resources):
                    print(f"Here is your {requirement}. Enjoy!")
                    machine.update_resources(requirement, MENU, resources)

        decision_to_continue = input("Do you have any more orders? Type 'Yes' or 'No'-> ").lower()
        while decision_to_continue not in ['yes', 'no']:
            if decision_to_continue not in ['yes', 'no']:
                print("Please provide a valid input ('Yes' or 'No')")
                decision_to_continue = input("Do you have any more orders? Type 'Yes' or 'No'-> ").lower()
        if decision_to_continue == 'no':
            orders = False


start_machine()
