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
    ordering_phase = True
    while ordering_phase == True:
        order = input("What would you like? (espresso/latte/cappuccino):")
        def report():
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        
        # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        # make this promt show again once the order is complete.
        
        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt
        if order == 'off':
            continue_order = False
            ordering_phase = False
        
        # TODO 3. Print report.
        elif order == 'report':
            report()
        else:
            ordering_phase = False
    
    # TODO 4. Check resources sufficient?
    def check_resources(order):
        if MENU[f"{order}"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            continue_order = False
        elif order == "latte" or order == "cappuccino" and MENU[f"{order}"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            continue_order = False
        elif MENU[f"{order}"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            continue_order = False
        elif order == 'off':
            return
    
    check_resources(order)
    
    # TODO 5. Process coins
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total_money = (quarters*.25)+(dimes*.1)+(nickels*.05)+(pennies*.01)
    
    # TODO 6. Check transaction successful?
    if total_money < MENU[f"{order}"]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    elif total_money >= MENU[f"{order}"]["cost"]:
        change = total_money - MENU[f"{order}"]["cost"]
        money += MENU[f"{order}"]["cost"]
        print(f"Here is ${change} in change.")
        
        # TODO 7. Make Coffee.
        print(f"Here is your {order} ☕. Enjoy")
        