import random

# J, Q, K are considered as 10 for blackjack
cards = {
    "Spades": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 
    "Clubs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Diamonds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
    "Hearts": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'],
}

clubs = ["Spades", "Clubs", "Diamonds", "Hearts"]

def my_cards(card):
    my = []
    for i in range(2):
        my.append(random.choice(cards[random.choice(clubs)])) # random.choice(clubs)- access club list, outer random picks one value
    return my

def comp_cards(card):
    comp = []
    for i in range(2):
        comp.append(random.choice(cards[random.choice(clubs)]))
    return comp
            
my_list = my_cards(cards)
comp_list = comp_cards(cards)

def draw(my_list, comp_list):
    my_sum = 0
    comp_sum = 0
    draws = True
    while draws == True:
        if my_list.__add__() < 21 or comp_list.__add__() < 21:
            my_sum = my_list.__add__()
            comp_sum = comp_list.__add__()
            print(my_sum, comp_sum)


draw(my_list, comp_list)
        



