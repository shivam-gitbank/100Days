# Random library pactice - Day 04

import random
num = random.randint(1,5) # choose a number inclusive of the range given - 1, 5 included
ran_num = random.random() * 10 # generates a number between 0.0 and 1.0 - the result cannot be equal to 1.0 its always less than that 
ran_flo = random.uniform(1, 10) # generates random float numbers inclusive of the range (a, b) included
print(f"num is {num} and ran_int = {ran_num}") 