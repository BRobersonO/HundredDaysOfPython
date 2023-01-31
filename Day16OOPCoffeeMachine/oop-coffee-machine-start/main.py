from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu = Menu()
myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()

is_on = True
while is_on:
    response = input(f"What would you like? ({myMenu.get_items()}) ")
    if response == "off":
        # turns machine off
        is_on = False
    elif response == "report":
        # print reports
        myCoffeeMaker.report()
        myMoneyMachine.report()
    else:
        # make orders: check resources, process coins, check transaction, make coffee
        item = myMenu.find_drink(response)
        if item == None:
            continue
        if not myCoffeeMaker.is_resource_sufficient(item):
            continue
        if not myMoneyMachine.make_payment(item.cost):
            continue
        myCoffeeMaker.make_coffee(item)
