# encoding logic - encrytption of text 
def encode():
    base_text = input("Type your message\n").lower()
    shift_number = int(input("Type the shift number\n"))
    cypher_text = ""
    for e in base_text:
        if e >= chr(97) and e <= chr(123):
            cypher_text += chr(ord(e) + shift_number)
    return cypher_text    

cy = encode()
print(cy)    