# used Dictionary of dictonaries, earlier was a list containing dictoary but due to indexing it was a bit tricky to search through the orders
CM_data = {
"Espresso": {
"water_intake": 50,
"milk_intake": 0,
"coffee_intake": 18,
"price": 1.50
},

"Latte": {
"water_intake": 200,
"milk_intake": 150,
"coffee_intake": 24,
"price": 2.50
},

"Cappuccino": {
"water_intake": 250,
"milk_intake": 100,
"coffee_intake": 24,
"price": 3.00
},

"report" :{"milk": 200,
"water": 300,
"coffee": 100 ,
"money": 0,}
}

coin_data = {"penny": 0.01, "Nickel": 0.05, "Dime" : 0.10, "Quarter": 0.25}

class Incorrect_order(Exception):
    pass

class Insufficient_resources(Exception):
    pass

class Money_error(Exception):
    pass