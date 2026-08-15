def add (n1, n2):
    return (n1+n2)

def subtract (n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def multiply (n1, n2):
    return n1*n2

operation = {
'+' : add,
'-' : subtract,
'*' : multiply,
'/' : divide,
}

val1 = int(input("enter your value = "))
aggregate = True
while aggregate == True:
    operator = input("choose your operator = ")
    val2 = int(input("enter second value = "))
    result = operation[operator](val1, val2)
    print(f"{val1} {operator} {val2} = {result}")
    cont = input("to continue with result press 'y' to start new cal press 'n' ")
    if cont == 'y':
        val1 = result
        continue
    elif cont == 'n':
        val1 = int(input("enter value = "))
        continue
    else:
        aggregate = False
        print("Oops wrong option chosen try again :)")
