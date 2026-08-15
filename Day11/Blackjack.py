import random

# J, Q, K are considered as 10 for blackjack
cards = {
    "Spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 
    "Clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
}

clubs = ["Spades", "Clubs", "Diamonds", "Hearts"] # list of keys to access card numbers, another way would  have been 2 list

def my_cards(card):
    my = []
    for i in range(2):
        chosen_card = random.choice(cards[random.choice(clubs)])# random.choice(clubs)- access club list, outer random picks one value
        if chosen_card == 'J' or chosen_card == 'K' or chosen_card =='Q': # Black jack J, K, Q logic
            my.append(10)
        else:
            my.append(chosen_card)
    return my

def comp_cards(card):
    comp = []
    for i in range(2):
        chosen_card = random.choice(cards[random.choice(clubs)])# random.choice(clubs)- access club list, outer random picks one value
        if chosen_card == 'J' or chosen_card == 'K' or chosen_card =='Q':
            comp.append(10)
        else:
            comp.append(chosen_card)
    return comp

def draw_more()
            
my_list = my_cards(cards)
comp_list = comp_cards(cards)

def draw(my_list, comp_list):
    my_sum = sum(my_list)
    comp_sum = sum(comp_list)
    draws = True
    while draws == True:
        if my_sum < 21 and comp_sum > 21:
            draws = False
            print("YOU WIN $$$ !!! :)")
        elif my_sum > 21 and comp_sum < 21:
            draws = False
            print("YOU LOSE :*( ")
        elif my_sum < 21 and comp_sum < 21:
            draws = True
            my_sum1, comp_sum1 = draw_more(my_sum, comp_sum)
draw(my_list, comp_list)
        



