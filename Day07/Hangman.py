#importing random for randomising list
import random

# list of random words to choose from for the problem 
word_list = ['family', 'donkey', 'hardware', 'xerox', 'transistor', 'computer',
 'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 
 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 
 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 
 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 
 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 
 'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 
 'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 
 'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser',
 'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen',
 'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest',
 'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket',
 'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph',
 'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 
 'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 
 'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 
 'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 
 'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter', 
 'classification', 'typewriter', 'success', 'difference', 'acoustics', 
 'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 
 'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 
 'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment', 
 'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection',
 'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn',
 'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment', 
 'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health', 
 'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet'
 'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object', 
 'tower', 'question', 'problem', 'pressure', 'beast', 'encouragement', 'afraid', 
 'cavity', 'appearance', 'wonderful', 'matter', 'dimension', 'business', 'doubt',
 'conversation', 'reaction', 'psychology', 'superstition', 'smash', 'horseshoe', 
 'surprise', 'nothing', 'ladder', 'opposite', 'reality', 'genius', 'string', 
 'attraction', 'sensitivity', 'magnification', 'someone', 'symptom', 'recipe',
 'service', 'family', 'island', 'planet', 'butterfly']
           

# The random word for the game 
Hangman_secret = random.choice(word_list)

# User input and instructions 
Name = input ("greetings what is your name ah!!!! :- ")
print(f"{Name}, we will let you guess the words for HANGMAN! you have 4 life lines with you"
      "\nif you guess incorrectly you will lose a life and the hangman shall be drawn")

# Place holder was required to hold display values and edge cases 
place_holder = ""
for x in Hangman_secret:
    place_holder += "_"

# Life Count
LIFE_COUNT = 3
guessed_letters = []

# logic for keeping the game going till life count is not zero
while LIFE_COUNT > 0: 
    # Keeping the input as lowercase to keep the input consistent.
    guess = input("\nwhat is your current guess? ").lower()
    display = ""
    # Gussed letters list for keeping correct gusses saved
    for letter in Hangman_secret:
        if guess == letter:
            guessed_letters.append(letter)

#   Loosing life logic  ( point left to correct - incorrect answers dont hold on to the state of display )           
    if guess not in Hangman_secret:
        LIFE_COUNT -= 1
        display = place_holder
        # handling incorrect answers 
    else: 
       # Dynamic display for guessed lettes 
       for s in Hangman_secret:
            if s in guessed_letters:
                display += s
            else:
                display += "_"
    place_holder = display
    print(display)
    # Game won logic 
    if "_" not in display:
        print(f"checkpoint --> {display}")
        break
    continue

if LIFE_COUNT == 0:
    print("your life are exhausted and so are you")
else:
    print(f"YOU WON!! the correct word is {Hangman_secret}")
