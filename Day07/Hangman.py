#importing random for randomising list
import random

# list of random words to choose from for the problem 
word_list = ['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer',
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

# the random word for the game 
Hangman_secret = random.choice(word_list)

# user input and instructions 
Name = input ("greetings what is your name ah!!!! ")
print(f"{Name}, we will let you guess the words for HANGMAN! you have 4 life lines with you \n"
      "if you guess incorrectly you will lose a life and the hangman shall be drawn\n ")

# total life 
LIFE_COUNT = 4

# logic 
while LIFE_COUNT > 0: 
    # Keeping the input as lowercase to keep the input consistent.
    guess = input("\nwhat is your current guess? ").lower()
    occurance = 0
    #logic for priting same lenght blanks and letters inside the random chosen word 
    for i, letter in enumerate(Hangman_secret):
        if guess == letter:
            print(letter, end= "")
            occurance += 1
        else:
            print("_",end= "")
    if occurance == 0:
        LIFE_COUNT -= 1
    else:
        continue


# approach now - should i keep a counter of yay nay and if nay == len of secret then no guess was correct - lose a life pop the letter - from the secret and add the letter
# to the same position as the secret word 

print(f"\n{Hangman_secret}")

if LIFE_COUNT == 0:
    print("your life are exhausted and so are you")
else:
    print(f"you got it right the correct word is {Hangman_secret}")
