import random

print("Welcome to the Password Generator !")
letters = int(input("How many Letters would you like in your password?\n"))
symbols = int(input("How many Symbols do you want in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

pas_len = letters + symbols + numbers

Symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '{', '}', '[', ']', '<', '>', '?']
letter_list = ['a','b','c','d','e','f','g','h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password = ''

for i in range(pas_len):
    s1 = random.choice(Symbol_list)
    password += s1

print(f"{password}")