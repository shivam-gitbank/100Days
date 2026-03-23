# Treasure island project - day 3 
print("Welcome to Treasure Island. \nYour mission is to find the treasure! ")

#conditionals 
direction = input("You are at a cross road. Where do you want to go? Type \"Left\" or \"Right\" ? \n")
if direction == "left":
    action = input("you come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat or Type \"swim\" to swim accross \n")
    if action == "wait":
        colour = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which colour do you choose? \n")
        if colour == "red":
            print("It's a room full of fire. Game Over.... :_(")
            exit
        elif colour == "blue":
            print("Its the endless pit. Game Over..... :L ")
            exit
        elif colour == "yellow":
            print("YOU FINALLY FOUND THE TREASURE -- YOU WON !!!! ")
            exit
    elif action == "swim":
        print ("you got eaten by a shark, come on bro, Game Over }:P ")
        exit
elif direction == "Right":
    print("get yo ass to bed now ")
    exit 
    

                
