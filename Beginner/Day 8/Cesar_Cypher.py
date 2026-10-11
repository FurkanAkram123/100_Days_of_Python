import art

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    result = ""
    if direction == "decode":
        shift = -shift

    for element in text:
        if element in alphabet:
            next_index = (alphabet.index(element) + shift) % 26
            new_char = alphabet[next_index]
            result += new_char
        else:
            result += element
    return result


print(art.logo)

#ask the user for their name and greet them
name = input("Welcome to the Caesar Cipher! Can i please get your name: ")
print (f"Hello {name}, let's get started!")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encoded_text = caesar_cipher(text, shift, direction)
    print(f"The {direction}d text is: {encoded_text}")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() != "yes":
        print("Goodbye!")
        break