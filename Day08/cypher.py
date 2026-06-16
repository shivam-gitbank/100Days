def encode():
    encode_text = input("Type your message\n")
    shift_number = input("Type the shift number").isdigit
    print(encode_text)
    for e in encode_text:
        cypher = e+shift_number
        print(cypher, end="")

encode()
    
    