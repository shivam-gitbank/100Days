# calculator logic
def calculator(val1, opr, val2):
    result = 0
    if opr == '+':              # add
        result = val1 + val2
    elif opr == '-':            # subtract
        result = val1 - val2
    elif opr == '*':            # multiply
        result = val1 * val2
    elif opr == '/':            # divide
        result = val1 / val2
    elif opr == '%':            # percentage
        result = val1 / (val2 * 100)
    return result

# While loop condition 
repeat = True
while repeat == True: 
    value = int(input("Please enter your value"))
    operator = input("Please specify the operation  '+', '-', '*', '/' '%' ") # operator
    val2 = int(input("Enter the value for operation"))
    final_val = calculator(value, operator, val2)
    print(f"the output is {value} {operator} {val2} = {final_val}")

# continuation logic for previous result set
    conti = input("do you wish to continue with the same result")
    if conti == 'yes':
        opr2 = input("specify operator")
        val3 = int(input("enter value to continue"))
        final_val2 = calculator(final_val, opr2, val3)
        repeat = True
        print(f"the output is {final_val} {operator} {val3} = {final_val2}")
    else:
        print(f"Power off, good bye!  :)")
        repeat = False
    
