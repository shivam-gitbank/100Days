# importing Random Liberary 
import random

# inputs from users
print("Welcome to the Password Generator !")
letters = int(input("How many Letters would you like in your password?\n"))
symbols = int(input("How many Symbols do you want in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

# List for every element required to create password
Symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '{', '}', '[', ']', '<', '>', '?']
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password = []

# Creating inital password with lists of letters, numbers and symbols
for i in range(letters):
    password.append(random.choice(letter_list))
for j in range(symbols):
    password.append(random.choice(Symbol_list))
for k in range(numbers):
    password.append(random.choice(numbers_list))

# Inital password created by random choice 
print(f"{password}")

# Randomizer Logic
def rand_pass(password1):
    len_pass = len(password1)
    pass_str =  ''
    for l in range(len_pass):
        R_pass = random.choice(password1)
        password1.remove(R_pass)
        pass_str += R_pass
    return pass_str

# calling out password randomizer logic
f_pass = rand_pass(password)
print(f"final password is {f_pass} ")