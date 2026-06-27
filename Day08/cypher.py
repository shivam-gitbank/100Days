# encoding logic - encrytption of text 
def encode():
    base_text = input("Type your message\n")
    shift_number = int(input("Type the shift number\n"))
    cypher_text = ""
# Loop for processing each letter in cypher 
    for e in base_text:
        t = chr(ord(e) + shift_number)
        if t >= chr(65) and t <= chr(90):
            cypher_text += t
        elif t >= chr(97) and t <= chr(122):
            cypher_text += t
        # Z letter edge case 
        else:
            cypher_text += chr(ord(t) - 26)
    return cypher_text    

# Decypher logic 
def decode(text, shift):
    decypher = ""
    # loop for decyphering 
    for t in text:
        if t <= chr(90) and t >= chr(65):
            decypher += chr(ord(t) - shift) 
        elif t <= chr(122) and t >= chr(97):
            decypher += chr(ord(t) - shift)
        else:
            decypher += chr(ord(t) + 26)
    return decypher

# choosing logic between Cypher and Decypher 
print("Welcome to Ceaser's cypher")
#Choice logic 
choice = int(input("what would you like to do" \
"\n 1 - Cypher text" \
"\n 2 - Decypher text\n"))

# function calling 
if choice == 1:
    print(encode())
else:
    print("To decypher text we need the text and the shift secret")
    decypher = input("Decypher text here --> ")
    shift_d = int(input("enter shift number "))
    print(decode(decypher, shift_d))