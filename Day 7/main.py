import random
from Stages_ASCII_Art import stage, logo
from words import word_list

# Ascii art for the hangman stages

#total number of lives
lives = 5

#Generate a random word from the list
random_word = random.choice(word_list)

# Create the beginning of the hangman game
print("Welcome to Hangman!", logo)
input("Press Enter to start the game...")

# Create a display string to show the correctly guessed letters and underscores for the remaining letters
display = ""

# Create a list to keep track of the correctly guessed letters and all the guessed letters
correct_guess = []
all_guesses = []

# create a boolean variable to check if the guessed letter is correct or not
correct = False

#check if the guessed letter is in the random word and update the display string
while lives>0:
    guessed_char = input("Guess a letter: ").lower()
    
    # Check if the guessed character has already been guessed, if it has, print a message and set the correct variable to True to skip the rest of the loop
    if guessed_char not in all_guesses:
        all_guesses.append(guessed_char)
    else:
        print("You have already guessed that letter!")
        correct = True

    # Check if the guessed character is in the random work and update the correct_guess list
    for letter in random_word:
        if letter == guessed_char:
            if letter not in correct_guess:
                correct_guess.append(guessed_char)
                correct = True
            elif letter in correct_guess:
                print("You have already guessed that letter correctly!")
                correct = True
            
        
    # Update the display string based on the correct_guess list
    for letter in random_word:
            if letter in correct_guess:
                display += letter
            else:
                display += "_"

    # If the guessed character is not correct, reduce the number of lives
    if correct == False:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    #print the current stage of the hangman and the display string
    print(stage[6-lives], f"The word to guess is: {display}", "\n", "*"*20, f"You have {lives} lives left.", "*"*20)

    # Check if the display string is equal to the random word, if it is, break the loop and end the game
    if display == random_word:
        print("Congratulations! You guessed the word correctly!")
        break

    # If the number of lives is 0 and the display string is not equal to the random word, print the game over message and the correct word
    elif lives == 0 and display != random_word:
        print (stage[6])
        print(f"Game over! The correct word was: {random_word}")

    # Reset the display string and correct variable for the next guess
    display = ""
    correct = False



