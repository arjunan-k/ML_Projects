from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
m = Menu()

is_on = True
while is_on:
    user_input = input(f"What would you like to order? {m.get_items()}: ")

    if user_input == "off":
        is_on = False

    elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        user_choice = m.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(user_choice):
            if money_machine.make_payment(user_choice.cost):
                coffee_maker.make_coffee(user_choice)

    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        m.find_drink(user_input)