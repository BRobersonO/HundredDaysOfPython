MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300, # original 300
    "milk": 200, # original 200
    "coffee": 100, # original 100
}

money = 0.00

def areEnoughResources(drinkOrder):
    for ingredient in MENU[drinkOrder]['ingredients']:
        if resources[ingredient] < MENU[drinkOrder]['ingredients'][ingredient]:
            print(f"Sorry, there isn't enough {ingredient} to make this drink.")
            return False
    return True

def takePayment(drinkOrder):
    quarters    =   float(input(f"How many quarters are you inserting? "))
    dimes       =   float(input(f"How many dimes are you inserting? "))
    nickles     =   float(input(f"How many nickles are you inserting? "))
    pennies     =   float(input(f"How many pennies are you inserting? "))
    payment     =   quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
    if MENU[drinkOrder]['cost'] > payment:
        print(f"Sorry, but that's not enough money to buy a {drinkOrder}. Money refunded.")
    else:
        if payment != MENU[drinkOrder]['cost']:
            change = payment - MENU[drinkOrder]['cost']
            global money
            money += MENU[drinkOrder]['cost']
            print (f"Awesome! Here is ${change:.2f} in change.")
        else:
            print (f"Awesome!")

def makeCoffee(drinkOrder):
    for ingredient in MENU[drinkOrder]['ingredients']:
        resources[ingredient] -= MENU[drinkOrder]['ingredients'][ingredient]
    print(f"Here is your {drinkOrder}. Enjoy!")

def unit (val):
    if val == "coffee":
        return "g"
    else:
        return "mL"

def coffeeMachine():
    # Get input for menu item or off/report command
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if areEnoughResources(choice):
            takePayment(choice)
            makeCoffee(choice)
            coffeeMachine()
        else:
            coffeeMachine()
    else:
        match choice:
            case "off":
                # End the program
                return 1
            case "report":
                # Print out a reportt on remainng resources
                print('\033[1m' + 'Ingredients Remaining:' + '\033[0m')
                for key, value in resources.items():
                    print(f"\t{key.capitalize() + ':':<10} {value} {unit(key)}")
                print('\033[1m' + 'Profit:' + '\033[0m')
                print(f"\t{'Money:':<9} ${money:.2f}")
                coffeeMachine()
            case _:
                print("Invalid Response")
                coffeeMachine()

coffeeMachine()