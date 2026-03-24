# # ticket counter code challenge 1 

print("Welcome to the roller coaster !! ")
height = float(input("What is your height in cm ? \n"))

# conditional to check for the minimum required height
if height < 120:
    print("Sorry your height does not qualify please visit again when you are taller !\n")
else:
    age = int(input("what is your age ? \n"))
# age check 
    if age <= 18:
        print("please pay $7.00 ")
    elif age > 18:
        print("please pay $12.00  ")
    print("enjoy your ride :)\n")


#coding challenge 2 ODD even check

# num = int(input("enter your desired number : "))
# if num % 2 == 0:
#     print("the number is even")
# else:    
#     print("number is odd")