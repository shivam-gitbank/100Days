import random
# Rock Paper Scissor mini project 
rock = ('''
    _______ROCK
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper = ('''
         PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
     
      ''')

scissors = ('''
            SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)  
      
      ''')
# storing ascii art in a list 
options = [rock,paper,scissors]

# getting user input
print("UP for a Rock Paper Scissors game ya ! ")
choice = input("What do you choose 'Rock', 'Paper', 'Scissors' \n").lower()
pc_option = random.choice(options)

#player choice converter and sanity check 
if choice == 'rock':
    choice = rock
elif choice == 'scissors':
    choice = scissors
elif choice == 'paper':
    choice = paper
else:
    print(f"incorrct input {choice}")

# rock paper and scissors conditional function 
def RPS_logic(P1,PC):
    if P1 == rock and PC == paper:
        print(f"({PC} beats {P1} - PC won")
    elif P1 == paper and PC == scissors:
        print(f"{PC} beats {P1} - PC won")
    elif P1 == scissors and PC == rock:
        print(f"{PC} beat {P1} - PC won")
    elif P1 == PC:
        print("you and PC are thinking alike")
    else:
        if P1 in options:
            print(f"{P1} won over {PC}- Player won")
        else:
            print(f"your input is not a vaild input {P1}")

RPS_logic(choice, pc_option)

