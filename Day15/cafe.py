import coffeedata
import random
MENU = coffeedata.CM_data # coffee menu
RESOURCES = coffeedata.CM_data["report"] # default value for resources
BALANCE = coffeedata.CM_data["report"]["money"] # coin values, in float (0.01, 0.05, 0.10, 0.25)
STOCK = True

# Resources Processing logic
def resources_processing(resources, order):
    milk = resources["milk"] - order["milk_intake"]
    water = resources["water"] - order["water_intake"]
    coffee = resources ["coffee"] - order["coffee_intake"]
# resources expection handling per inventory item
    try:
        if milk < order["milk_intake"]:
            STOCK = False
            raise coffeedata.Insufficient_resources("Milk Insufficent! cannot process order kindly restock")
        elif water < order["water_intake"]:
            STOCK = False
            raise coffeedata.Insufficient_resources("Water Insufficient! cannot process order kindly refill") 
        elif coffee < order["coffee_intake"]:
            STOCK = False
            raise coffeedata.Insufficient_resources("Coffee Insufficient to process order, kindly restock!")
        else:
            print("Enjoy your Coffee!")
    except coffeedata.Insufficient_resources as e:
            print(e) 

# Money and order processing
def process_order(price, order):
    # money def and calc
    Quarter = int(input("Enter the number of Quarters ")) * coffeedata.coin_data["Quarter"]
    Dime = int(input("Enter the number of Dime ")) * coffeedata.coin_data["Dime"]
    Nickel = int(input("Enter the number of Nickel ")) * coffeedata.coin_data["Nickel"]
    Penny = int(input("Enter the number of Penny ")) * coffeedata.coin_data["Penny"]
    total = (Quarter + Dime + Nickel + Penny) # total

    try:
        if total < price:
            raise coffeedata.Money_Error("Insufficient Money Provided! Please try again")
#    global declaration for passing 
        global BALANCE
        global RESOURCES
        BALANCE += total
        resources_processing(RESOURCES, order) # resources processing
    except coffeedata.Money_Error as e:
        print(e)

# REPEATED ORDER AND INCORRECT ORDER HANDLING
while STOCK == True:
    try:
        user_input = input("Please enter your choice of coffee \n 'Espresso', 'Latte', 'Cappuccino' ")
        if user_input not in (MENU.keys()):
            raise coffeedata.Incorrect_order("Oops! Incorrect Order, please try again.") 
        elif user_input == "report": # report logic
            report = MENU[user_input]
            STOCK = False
            print(report)
        else:
            final = process_order(MENU[user_input]["price"], MENU[user_input]) # ACCESSING ORDER PRICE PASSING TO ORDER PROCESSING LOGIC
            print(final)
    except coffeedata.Incorrect_order as e:
                print(e)