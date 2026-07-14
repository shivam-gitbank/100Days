# encoding logic - encrytption of text 
def encode():
    base_text = input("Type your message\n")
    shift_number = int(input("Type the shift number\n"))
    cypher_text = ""
# Loop for processing each letter in cypher 
    for e in base_text:
        t = chr(ord(e) + shift_number) # disrupting space and special chars!!
        if t >= chr(65) and t <= chr(90):
            cypher_text += t
        elif t >= chr(97) and t <= chr(122):
            cypher_text += t
        # Z letter edge case 
        elif t > 'z' or t > 'Z':
            cypher_text += chr(ord(t) - 26)
        else:
            cypher_text += e
    return cypher_text    

# Decypher logic 
def decode(text, shift):
    decypher = ""
    # loop for decyphering 
    for t in text:
        de = chr(ord(t) - shift)
        print(de,"--->",  t) # if t = a and de = a - x t = a then a +26 - split 
        if de > 'Z' and de < 'a':
            decypher += chr(ord(de) + 26) 
            print(de,"---> Between a and z",  t)
        elif de >= 'a' and de <= 'z':
            decypher += de 
            print(de,"--->",  t)
        elif de >= 'A' and de <= 'Z':
            decypher += de
            print(de,"---> between A and Z",  t)
        elif de < 'A':
            decypher += chr(ord(de) + 26)
            print(de,"---> - <A logic",  t)
        elif de.isalpha != True:
            decypher += t
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