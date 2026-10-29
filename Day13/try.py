#booze logic
def booze(age):
      if age > 18:
            print("you are allowed to drink booze ")
      else:
            print(f"your age is {age} and are younger than 18 not allowed to drink")

#expection handling
try:
    age = int(input("enter your age "))
    booze(age)
except ValueError:
    print("Enter a valid age eg 19")
    age = int(input("enter age again "))
    booze(age)