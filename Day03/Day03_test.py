# # ticket counter code challenge 1 

print("Welcome to the roller coaster !! ")
height = float(input("What is your height in cm ? \n"))
bill = 0

# conditional to check for the minimum required height
if height < 120:
    print("Sorry your height does not qualify please visit again when you are taller !\n")
else:
    age = int(input("what is your age ? \n"))
# age check 
    if age <= 12:
        bill = 5.00
        print(f"tickets for minors are $ {bill}")
    elif age <= 18:
        bill = 7.00
        print(f"tickets for teens are $ {bill}")
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12.00
        print(f"tickets for Adults are $ {bill}")

# logic for photos
    decision = input("do you want to photos of your ride ? ")
    if decision.lower() == "yes":
        bill += 3.00

print(f"total bill is $ {bill}")
print("enjoy your ride :)\n")


#coding challenge 2 ODD even check

# num = int(input("enter your desired number : "))
# if num % 2 == 0:
#     print("the number is even")
# else:    
#     print("number is odd")