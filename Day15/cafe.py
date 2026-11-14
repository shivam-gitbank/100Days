import coffeedata
import random
MENU = coffeedata.CM_data # coffee menu
MONEY = coffeedata.coin_data # coin values, in float (0.01, 0.05, 0.10, 0.25)



def process_order(user_input):
    print(MENU[user_input])

# def menu():

# def money():


user_input = input("Please enter your choice of coffee \n 'Espresso', 'Latte', 'Cappuccino' \n")

# incorrect order handling
try:
    if user_input not in (MENU.keys()):
        raise coffeedata.Incorrect_order("Oops! Incorrect Order, please try again.")
    else:
        if user_input in (MENU.keys()): # matching string with in keyword inside menu with keys menthod
            process_order(user_input)
except coffeedata.Incorrect_order as e:
    print(e)