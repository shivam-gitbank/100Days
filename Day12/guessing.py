import random

# Randomly produces number
final_number = int(random.random()* 100)  

# Choosing difficulty 
difficulty = input("choose your difficulty \n" \
" --> HARD (┬┬﹏┬┬)\n" \
"---> EASY o(≧▽≦) \n").lower()

# chances logic
if difficulty == "hard":
    chances = 5
else:
    chances = 10

# guess function global scope 
def Guess():
    num = int(input("Enter your number -->"))
    return num

# function for difficulty and continuing the game
def game(chances):
    guess = Guess()
    while chances >= 2:
        if guess == final_number:
            print("you guesssed it right")
        elif guess < final_number:
            chances -= 1
            print("your guessed too low \n" \
            f"you now have {chances} chances")
            guess = Guess()                  
        elif guess > final_number:
            chances -=1
            print("you guessed too high\n" \
            f"now you have {chances} chances")
            guess = Guess()
    if chances <= 2:
        print(f"Game over correct answer was {final_number} ")
game(chances)