from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

while machine_on:
    drink_m = Menu()
    cm = CoffeeMaker()
    cmm = MoneyMachine()
    #cmmm = MenuItem()
    drink = input(f"What would you like? {(drink_m.get_items())}: " ).lower()



    if drink == "off":
        machine_on = False
    elif drink == "report":
        cm.report()
        cmm.report()
    else:
        if drink_m.find_drink(drink) == "Sorry that item is not available.":
            machine_on = True
        #cm.is_resource_sufficient(drink)
        else:
            drink_f = drink_m.find_drink(drink)
            if  cm.is_resource_sufficient(drink_f):
                price = drink_f.cost

                if cmm.make_payment(price):
                    cm.make_coffee(drink_f)
                else:
                    machine_on = True




