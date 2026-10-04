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

#Draw logic
def draw(my_list, comp_list):
    my_sum = sum(my_list)
    comp_sum = sum(comp_list)
    print(f"your current card total = {my_sum} \nopp current cards sum = {comp_sum}\n")
    choice = input("do you wish to draw more cards ? Yes - y or No - n ").lower()

    #while logic
    while choice == 'y'and my_sum < 21 and comp_sum < 21:
        my_list.append(random_cards())
        comp_list.append(random_cards())
        my_sum = sum(my_list)
        comp_sum = sum(comp_list)
        print(f"updated totals \nopp total = {comp_sum}\n your total = {my_sum}")
        if my_sum > 21 and comp_sum <= 21:
            print("you lose, went over 21")
        elif my_sum <= 21 and comp_sum > 21:
            print("you won")
        elif my_sum == comp_sum and my_sum < 21:
            print("its a draw ")
        elif my_sum < 21 and comp_sum < 21:
            choice = input("do you wish to draw again , y or n -> ")
        elif my_sum == 21:
            print("you at 21 exactly you won")
        else:
            print("you both went over 21")

    if choice == 'n' and my_sum < 21 and my_sum > comp_sum:
        print("you won as you are closer to 21")
    elif choice == 'n' and my_sum < comp_sum and comp_sum < 21:
        print("you lose as you your opp is closer to 21")

draw(my_list, comp_list)

             

        



