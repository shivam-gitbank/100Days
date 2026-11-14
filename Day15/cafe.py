import coffeedata
import random
MENU = coffeedata.CM_data # coffee menu
DEF_REC = coffeedata.CM_data["report"] # default value for resources
MONEY = coffeedata.coin_data # coin values, in float (0.01, 0.05, 0.10, 0.25)


def report():
    print(DEF_REC)
# def resources():

# def menu():

# def money():


user_input = input("Please enter your choice of coffee \n 'Espresso', 'Latte', 'Cappuccino' \n")

# incorrect order handling
try:
    if user_input not in (MENU.keys()):
        raise coffeedata.Incorrect_order("Oops! Incorrect Order, please try again.")
    else:
        if user_input in (MENU.keys()): # matching string with in keyword inside menu with keys menthod
            print(MENU[user_input]) 
except coffeedata.Incorrect_order as e:
    print(e)