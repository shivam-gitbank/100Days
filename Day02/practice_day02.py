print("Numbers of letters in your name " + str(len(input("Enter your name "))))

# PEMDAS example and toutorial - the PEMDAS rule moves from left to right --> 
x = len(input("Enter: ")) * 2 + 3
print(x)

#pemdas to return output 3 
print((3 * ((3 + 3) / 3 )) - 3 )    


# quick BMI calclulator 
height = 1.8
wight = 74.3

def calc(h1, w1):
    return w1/(h1**2)

bmi = calc(height, wight)
print(round(bmi, 2))