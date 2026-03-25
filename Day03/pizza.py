# day 3 pizza project 
print("Welcome to Python Pizza Deliveries !")
size = input("What size of Pizza do you want? S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want Extra Cheese on your pizza> Y or N: ")
total_bill = 0

# pilot pizza project (conditional formatting)
if size == 'S':
    total_bill = 15
elif size == 'M':
    total_bill = 20
elif size == 'L':
    total_bill = 25
else:
    print("We know you are hungry but the incorrect pizza will only increase delay :)")# exception handler 

# Option for pepperoni
if pepperoni == 'Y':
    if size == 'S':
        total_bill += 2
    else:
        total_bill += 3

# Option for cheese 
if extra_cheese == 'Y':
    total_bill += 1

# final bill 
print(f"Your Final Bill is $ {total_bill}.")
    