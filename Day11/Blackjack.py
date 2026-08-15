import random

# J, Q, K are considered as 10 for blackjack
cards = {
    "Spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 
    "Clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
}

clubs = ["Spades", "Clubs", "Diamonds", "Hearts"] # list of keys to access card numbers, another way would  have been 2 list

def random_cards(card):
    my = []
    comp = []
    for i in range(2):
        my_card = random.choice(cards[random.choice(clubs)])# random.choice(clubs)- access club list, outer random picks one value
        comp_card = random.choice(cards[random.choice(clubs)])
        if my_card == 'J' or my_card == 'K' or my_card =='Q': # Black jack J, K, Q logic
            my.append(10)
        elif comp_card == 'J' or comp_card == 'K' or comp_card == 'Q':
            comp.append(10)
        else:
            my.append(my_card)
            comp.append(comp_card)
        return my, comp

def draw_more():
    return int(random.choice(cards[random.choice(clubs)]))
            
my_list, comp_list = random_cards(cards)

def draw(my_list, comp_list):
    my_sum = sum(my_list)
    comp_sum = sum(comp_list)
    draws = True
    while draws == True:
        if my_sum < 21 and comp_sum > 21:
            draws = False
            print(f"{my_sum}, {comp_sum}")
            print(f"YOU WIN $$$ !!! :)")
        elif my_sum > 21 and comp_sum < 21:
            draws = False
            print(f"{my_sum}, {comp_sum}")
            print(f"YOU LOSE :*( ")
        elif my_sum < 21 and comp_sum < 21:
            draws = True
            print(my_sum, comp_sum)
            newcard = draw_more()
            newcard1 = draw_more()
            my_sum += newcard
            comp_sum += newcard1
            print(f"{my_sum}, {comp_sum}")
draw(my_list, comp_list)
        



