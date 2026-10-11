import random

# List of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numbers and symbols to choose from
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols to choose from
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!" )

#Get the inpit from the user about how many letters, symbols and numbers they want in their password
nr_letters = int(input("How many letters would you like in your password?"))
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

# create an empty list to store the characters of the password
password = []

# Add the specified number of letters, symbols and numbers to the password list
for char in range(0, nr_letters):
    password.append(random.choice(letters))

for char in range(0, nr_symbols):
    password.append(random.choice(symbols))
    
for char in range(0, nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the password list to randomize the order of characters
random.shuffle(password)

#print the password by joining the characters in the list
print(f"Your password is: {''.join(password)}")


