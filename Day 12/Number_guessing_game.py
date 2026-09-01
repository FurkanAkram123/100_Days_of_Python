import random
import ASCII_Art
import os, subprocess

#print the welcome message
print (ASCII_Art.logo)

game_active = True
hard = 5
easy = 10

def start_game(difficulty, num):

    tries_valid = True
    if difficulty == "easy":
        max_tries = easy
    else:
        max_tries = hard

    while tries_valid:
        for i in range(max_tries, 0, -1):
            guess = int(input (f"you have {i} tries left. Make a guess: "))
            if guess == num:
                return f"Congrats, you guessed the correct number."
                break
            elif guess < num:
                print ("You guessed too low.")
            else:
                print ("You guessed too high")

        tries_valid = False
        return f"The number was {num}, You lose."
    
while game_active:
    num = random.randint(1,100)
    print ("I'm thinking of a number between 1 and 100.")

    #set the difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':" ).lower()
    print (start_game(difficulty, num))

    if (input("Would you like to play again? Type 'yes' or 'no': ")).lower() == 'no':
        game_active = False

# Clear the screen 
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) 
print ("Thank you for playing")

