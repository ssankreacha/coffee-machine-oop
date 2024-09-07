from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Construction of Objects to Class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = MenuItem(f'{menu.get_items()}', 'water', 'milk', 'coffee', 'cost')

is_on = True
while is_on:
    cost = menu_item.cost
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "report":
        coffee_maker.report()   # prints current report (water/milk/coffee)
        money_machine.report()  # prints current profit
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
