# encoding logic - encrytption of text 
def encode():
    base_text = input("Type your message\n").lower()
    shift_number = int(input("Type the shift number\n"))
    cypher_text = ""
    for e in base_text:
        t = chr(ord(e) + shift_number)
        if t >= chr(97) and t < chr(124):
            cypher_text += t
        else:
            cypher_text += (t - 27)
    return cypher_text    

cy = encode()
print(cy)    