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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
continue_order = True
while continue_order == True:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # make this promt show again once the order is complete.
    order = input("What would you like? (espresso/latte/cappuccino):")
    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
    if order == 'off':
        continue_order = False
    # TODO 3. Print report.
    elif order == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    # TODO 4. Check resources sufficient?
    def check_resources(order):
        if MENU[f"{order}"]["ingredients"]["water"] < resources["water"]:
            print("Sorry there is not enough water.")
    # TODO 5. Process coins
    # TODO 6. Check transaction successful?
    # TODO 7. Make Coffee.