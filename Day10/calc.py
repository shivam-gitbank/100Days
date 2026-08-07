
def calculator(val1, opr, val2):
    result = 0
    if opr == '+':
        result = val1 + val2
    elif opr == '-':
        result = val1 - val2
    elif opr == '*':
        result = val1 * val2
    elif opr == '/':
        result = val1 / val2
    elif opr == '%':
        result = val1 / (val2 * 100)
    return result

repeat = True
while repeat == True: 
    value = int(input("Please enter your value"))
    operator = input("Please specify the operation  '+', '-', '*', '/' '%' ")
    val2 = int(input("Enter the value for operation"))
    final_val = calculator(value, operator, val2)
    conti = input("do you wish to continue with the same result")
    print(f"")
    if conti == 'yes':
        opr2 = input("specify operator")
        val3 = int(input("enter value to continue"))
        final_val = calculator(final_val, opr2, val3)
        repeat = True
        print(f"")
    else:
        print(f"")
        repeat = False
    
