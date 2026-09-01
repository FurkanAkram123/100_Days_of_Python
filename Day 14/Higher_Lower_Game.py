import random
import Follower_data
import ASCII_Art
import os, subprocess

game_active = True
score = 0

#print the welcome message
print (ASCII_Art.logo)

def check_answer (num1, num2, answer):
    if answer == 1:
        if num1 >num2:
            return True
        else: return False
    elif answer == 2:
        if num2 >num1:
            return True
        else: return False
    else: return False

def higher_lower(key1, key2):
    global score
    name_1 = Follower_data.DATA[key1]["name"]
    name_2 = Follower_data.DATA[key2]["name"]
    follower_count_1 = Follower_data.DATA[key1]["follower_count"]  
    follower_count_2 = Follower_data.DATA[key2]["follower_count"]

    #try except statement in case the user enters an incorrect number
    try:
        answer = int(input (f"Who has the higher follower count between {name_1} and {name_2}? Type '1' for {name_1} or '2' for {name_2}: "))
    except ValueError or answer < 1 or answer > 2 :
        answer = int(input(f"You enter an invalid number, try again: "))

    #check if the user got the answer correct and send the results back
    return check_answer (follower_count_1, follower_count_2, answer)

#main function
def main():
    global game_active
    global score
    game_running = True

    while game_active:
 
        while game_running:
        # Get an index number for the key we will use and make sure it's not the same.
            while True:
                key_num_1 = random.randint(0, len(Follower_data.DATA)-1)
                key_num_2 = random.randint(0, len(Follower_data.DATA)-1)

                if key_num_1 != key_num_2:
                    break

            #increase the score by one if the user got it right
            if higher_lower(key_num_1,key_num_2):
                score += 1
                print (f"correct, you're current score is {score}")
            else: 
                print (f"Incorrect, you're final score is {score}")
                game_running = False

        #once the game is done running, check if the user wants to play again
        if (input("Would you like to play again? Type 'yes' or 'no': ")) == "yes":
            game_running = True
        else: game_active = False
        score = 0

#This line prevents the code from running accidentally if this script is imported
if __name__ == "__main__":
    if (input("Would you like to play the higher/lower game? Type 'yes' or 'no':" ).lower() == "yes"):
        main()

        # Clear the screen once the game is done
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True) 
        print ("Thank you for playing!")
    else:
        
        print ("Goodbye!")