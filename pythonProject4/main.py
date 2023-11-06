
from collections import Counter
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

resources_report = {}

def insert_coin(type):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pinnies = int(input("how many pennies?: "))
    total_value = quarters*0.25 + dimes*0.1 + nickles*0.05 + pinnies*0.01
    if total_value >= MENU[type]['cost']:
        #order recieved
        resources_report['money'] += MENU[type]['cost']
        print(total_value)
        balance = total_value - MENU[type]['cost']
        print(f'you change ${balance}')
        print(f'here is your {type} enjoy it.')
    else:
        print("Sorry that's not enough money. Money refunded.")

def drink(type):
    ingredients1 = Counter(MENU[type]["ingredients"])
    resources1 = Counter(resources)
    if resources1['water'] > ingredients1['water'] and resources1['milk'] > ingredients1['milk'] and resources1['coffee'] > ingredients1['coffee']:
        resources_left = resources1 - ingredients1
        resources.update(resources_left)
        resources_report.update(resources)
        resources_report['money'] = 0
        print(resources_report)
        insert_coin(type)

    else:
        run = True
        for key in resources1:
            while run:
                if resources1[key] < ingredients1[key]:
                    print(f"Sorry there is not enough {key} ")
                    run = False


def ask():
    continue_mc = True
    while continue_mc:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            print(resources_report)
        elif choice == 'off':
            continue_mc = False
            print("Machine is off")
        elif choice == "espresso":
            drink('espresso')
        elif choice == 'latte':
            drink('latte')
        elif choice == 'cappuccino':
            drink('cappuccino')



#machine_on = True
# while machine_on:
#     if input()
print(resources)
ask()
