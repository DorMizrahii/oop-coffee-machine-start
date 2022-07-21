from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    off = False
    while not off:
        choice = input(f"What would you like to drink? {menu.get_items()} ")
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            print("Turning off, Good bye :)")
            off = True
        else:
            choice = menu.find_drink(choice)
            if choice and coffee_maker.is_resource_sufficient(choice):
                if money_machine.make_payment(choice.cost):
                    coffee_maker.make_coffee(choice)


coffee_machine()
