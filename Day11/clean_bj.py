import random

#const list
numbers =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# J, Q, K are considered as 10 for blackjack
cards = {
    "Spades":numbers, 
    "Clubs": numbers,
    "Diamonds": numbers,
    "Hearts": numbers,
}

#list of keys
clubs = ["Spades", "Clubs", "Diamonds", "Hearts"] # list of keys to access card numbers, another way would  have been 2 list

#picking random card from list 
def random_cards():
    the_card = random.choice(cards[random.choice(clubs)])# random.choice(clubs)- access club list, outer random picks one value
    if the_card == 'J' or the_card == 'K' or the_card =='Q': # Black jack J, K, Q logic
        the_card = 10
    return int(the_card)

# initial list prep
comp_list = []
my_list = []
opp_sum = -1
my_sum = -1
game_over = False #flag

# drawing 2 cards for both opp to start the game
for i in range(2): # choosing random 2 cards for both player and comp
    comp_list.append(random_cards())
    my_list.append(random_cards())

#calculate sum of cards - per list
def calculate_score (lst):
    if sum(lst) == 21 and len(lst) == 2:
        return 0
    if 11 in lst and sum(lst) > 21:
        lst.remove(11)
        lst.append(1)
    return sum(lst)

def compare(my_sum, comp_sum):
    if my_sum == comp_sum :
        return "Draw !"
    elif comp_sum == 21:
        return "opp has a blackjack"
    


while game_over == False:         
    opp_sum = calculate_score(comp_list)
    my_sum = calculate_score(my_list)
    print(f"your cards {my_list} - your score {my_sum}")
    print(f"your Opp first card {comp_list[0]}")
    # video lecture solution       
    if my_sum > 21:
        print("you lost as you went over 21")
        game_over = True
    else:
        choice = input('do you wish to draw another card "y" or "n" ')
        if choice == 'y':
            my_list.append(random_cards())
        else:
            game_over


while opp_sum != 0 and opp_sum < 17:
    comp_list.append(random_cards())
    opp_sum = calculate_score(comp_list)