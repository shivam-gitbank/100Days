alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# cypher logic
def ceaser(choice_text, text_input, shift_number):
    output_text = ""
    if choice_text == 'decode':
        shift_number *= -1
    for letter in text_input:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_number
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text

# While loop to continue decyphering 
Restart = True
while Restart:
    choice = input("for encoding type 'encode' for decypting type 'decode' \n").lower()
    text = input("Input your text here \n").lower()
    shift = int(input("enter your shift number \n"))

    # Cypher at work
    final_text = ceaser(choice_text = choice, text_input = text, shift_number = shift)
    print(f"the {choice}d text is {final_text}\n")

    # logic to re run
    rerun = input("do you wish to rerun ").lower
    if rerun == 'no':
        print("good bye!")
        Restart = False
        