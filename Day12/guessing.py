import random

#randomly produces number
final_number = int(random.random()* 100)  

difficulty = input("choose your difficulty \n" \
" --> HARD (┬┬﹏┬┬)\n" \
"---> EASY o(≧▽≦) \n").lower()

if difficulty == "hard":
    chances = 5
    guess = input("enter your number")
    for i in range(chances):
        if guess == final_number:
            print("you guesssed it right")
        else:
            chances -= 1
            print("your guess was incorrect Guess again\n" \
            f"you now have {chances}")
            if chances == 0:
                print("game over ")
                break
else:
    chances = 10
    guess = input("enter your number")
    for i in range(chances):
            if guess == final_number:
                print("you guesssed it right")
            else:
                chances -= 1
                print("your guess was incorrect Guess again\n" \
                f"you now have {chances}")
                if chances == 0:
                    print("game over ")
                    break