print("Numbers of letters in your name " + str(len(input("Enter your name "))))
x = len(input("Enter: ")) * 2 + 3
print(x)
print((3 * ((3 + 3) / 3 )) - 3 )    

height = 1.8
wight = 74.3

def calc(h1, w1):
    return w1/(h1**2)

bmi = calc(height, wight)
print(round(bmi))