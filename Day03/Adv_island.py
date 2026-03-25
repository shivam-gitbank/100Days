# Treasure island project - day 3 
print("Welcome to Treasure Island. \nYour mission is to find the treasure! ")

#conditionals 
direction = input("You are at a cross road. Where do you want to go? Type \"Left\" or \"Right\" ? \n")
if direction.lower() == "left":
    action = input("you come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat or Type \"swim\" to swim accross \n")
    if action.lower() == "wait":
        colour = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose? \n")
        if colour.lower() == "red":
            print("It's a room full of fire. Game Over.... :_(")
        elif colour.lower() == "blue":
            print("Its the endless pit. Game Over..... :L ")
        elif colour.lower() == "yellow":
            print("YOU FINALLY FOUND THE TREASURE -- YOU WON !!!! ")
    elif action.lower() == "swim":
        print ("you got eaten by a shark, come on bro, Game Over }:P ")
else:
    print("GAME OVER - there was a lion waiting to eat you out there :()")

    

                
