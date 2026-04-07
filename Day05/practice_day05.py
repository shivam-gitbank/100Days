import random
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

student_scores = [45,34,63,43,6,67,5,34345,45,45,34,345,345,34,3,45345,345,34,5,345,34,543,5345]
max = 0 
for i in student_scores:
    if max < i:
        max = i
print(max)

go = random.random() * 10
print(go)

sum_100 = 0
for num in range(1, 101):
    sum_100 += num
print(sum_100)

# fizz buzz game
for inte in range(1, 101):
    if inte % 3 == 0 and inte % 5 != 0:
        print("Fizz")
    elif inte % 5 == 0 and inte % 3 != 0:
        print("Buzz")
    elif inte % 3 == 0 and inte % 5 == 0:
        print("FizzBuzz")
    else:
        print(inte)