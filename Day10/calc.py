
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
    
