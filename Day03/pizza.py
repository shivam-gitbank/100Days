# day 3 pizza project 
print("Welcome to Python Pizza Deliveries !")
size = input("What size of Pizza do you want? S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want Extra Cheese on your pizza> Y or N: ")
total_bill = 0

# pilot pizza project (conditional formatting)
if size == 'S':
    total_bill = 5
    if pepperoni == 'Y':
        total_bill += 3
    elif pepperoni == 'N':
        total_bill == total_bill
        if extra_cheese == 'Y':
            total_bill +=2
        elif extra_cheese == 'N':
            total_bill == total_bill
    print(f"price for small pizza is ${total_bill}") 
elif size == 'M':
    total_bill = 7
    if pepperoni == 'Y':
        total_bill += 3
    elif pepperoni == 'N':
        total_bill == total_bill
        if extra_cheese == 'Y':
            total_bill +=2
        elif extra_cheese == 'N':
            total_bill == total_bill
    print(f"price for Medium pizza is ${total_bill}")
elif size == 'L':
    total_bill = 10
    if pepperoni == 'Y':
        total_bill += 3
    elif pepperoni == 'N':
        total_bill == total_bill
        if extra_cheese == 'Y':
            total_bill +=2
        elif extra_cheese == 'N':
            total_bill == total_bill
            print(f"total bill is : $ {total_bill}")
    print(f"price for largeH pizza is ${total_bill}")
else:
    print("We know you are hungry but the incorrect pizza will only increase delay :)")
    