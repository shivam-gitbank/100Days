import random

print("Welcome to the Password Generator !")
letters = int(input("How many Letters would you like in your password?\n"))
symbols = int(input("How many Symbols do you want in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

Symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '{', '}', '[', ']', '<', '>', '?']
letter_list = ['a','b','c','d','e','f','g','h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for n in range(letters):
    let = random.choice(letter_list)
    password += let
    for i in range(symbols):
        sym = random.choice(Symbol_list)
        password += sym
        for k in range(numbers):
            numb = random.choice(numbers_list)
            password += numb

print(f"your password is {password}")


