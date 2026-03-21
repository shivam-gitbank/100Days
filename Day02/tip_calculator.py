# Tip Calculator 
print("Welcome to the Tip Calculator")

# Tip calculator program 
def tip_calc (bill, tip_percent):
    tip_tot = bill * tip_percent * 0.01
    return bill + tip_tot

# variable collection for calculation 
bill_total = int(input("What is your total bill? $"))
tip = int(input("How much tip would you like to give 10, 12 or 15% "))
total_BT = int(tip_calc(bill_total,tip))

# splitting bill logic 
peeps = int(input ("how may people you wanna split the bill with? "))
bill_per_persion = total_BT/peeps
print(f"Each persion should pay : ${bill_per_persion}")

