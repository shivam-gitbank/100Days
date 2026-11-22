import random
import gamedata

# score
score = 0

# inital conditions for comparison and game state
lose = False
option_1 = gamedata.data[int(random.random() * 100)]
option_2 = gamedata.data[int(random.random() * 100)]

while lose != True:
    # dictionary access to key
    print(f" Personality 1 \n {option_1['name']}, occupation --> {option_1['occupation']}")
    print(" VS ")
    print(f" Personality 2 \n {option_2['name']}, occupation --> {option_2['occupation']}")

    # choosing logic
    player_choice = input("Choose the personality with higher follower count: A or B ").lower()
    if player_choice == 'a':
        if option_1['followers'] > option_2['followers']:
            print("your guess was correct")
            score += 1
            option_2 = gamedata.data[int(random.random() * 100)]
        else:
            print("your guess was wrong")
            print("Game Over")
            print(f"your score is {score}")
            lose = True
    elif player_choice == 'b':
        if option_2['followers'] > option_1['followers']:
            print("your guess was correct")
            score += 1
            option_1 = option_2
            option_2 = gamedata.data[int(random.random() * 100)]
        else:
            print("your guess was wrong")
            print(f"your score is {score}")
            print("Game Over")
            lose = True
    else:
        print("Invalid input, please try again")