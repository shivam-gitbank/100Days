import random

# J, Q, K are considered as 10 for blackjack
cards = {
    "Spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 
    "Clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
}

clubs = ["Spades", "Clubs", "Diamonds", "Hearts"] # list of keys to access card numbers, another way would  have been 2 list

def random_cards():
    the_card = random.choice(cards[random.choice(clubs)])# random.choice(clubs)- access club list, outer random picks one value
    if the_card == 'J' or the_card == 'K' or the_card =='Q': # Black jack J, K, Q logic
        the_card = 10
    return int(the_card)

# initial list prep
comp_list = []
my_list = []
for i in range(2): # choosing random 2 cards for both player and comp
    comp_list.append(random_cards())
    my_list.append(random_cards())

def draw(my_list, comp_list):
    my_sum = sum(my_list)
    comp_sum = sum(comp_list)
    print(f"your current card total = {my_sum} \nopp current cards sum = {comp_sum}")
    choice = input("do you wish to draw more cards ? Yes - y or No - n ").lower()
    if choice == 'y' and my_sum < 21:
        my_list.append(random_cards)
        comp_list.append(random_cards)
        my_sum = sum(my_list)
        comp_sum = sum(comp_list)
        if my_sum == 21:
            print("you win {my_sum}")
    else:
        if my_sum < 21 and my_sum > comp_sum:
            print(f"you won as you are closer to 21 than your opp!")
        elif my_sum > 21 and comp_sum <= 21:
            print(f"you went over 21 you lose!")
        elif my_sum == comp_sum:
            print("its a draw ")
    
draw(my_list, comp_list)
            
        #     draws = False
        #     print(f"your cards sum {my_sum}, opp card sum {comp_sum}")
        #     print(f"YOU WIN $$$ !!! :)")
        # elif my_sum > 21 and comp_sum < 21:
        #     draws = False
        #     print(f"{my_sum}, {comp_sum}")
        #     print(f"YOU LOSE :*( ")
        # elif my_sum < 21 and comp_sum < 21:
        #     draws = True
        #     print(f"your sum {my_sum}, opp sum {comp_sum}")
        #     choice = input("do you wish to draw more press 'yes' else 'No'").lower()
        #     if choice == "yes":
        #         random_cards
             

        



