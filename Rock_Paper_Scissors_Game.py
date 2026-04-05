import random as ry
# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
# Keep asking the user for input until they provide a valid choice
while True:
    choice = input("Pick your choice, type 0 for Rock, 1 for Paper or 2 for scissors: ")
    if choice in ["0", "1", "2"]:
        break
    else:
        print("Invalid choice, please choose 0, 1 or 2")

# Get a random number for the computer
computer_choice = str(ry.randint(0,2))

#print the choices for the user and the computer
print(f"You chose {choice} and the computer chose {computer_choice}")

if (choice == "0" and computer_choice == "2") or (choice == "1" and computer_choice == "0") or (choice == "2" and computer_choice == "1"):
    print("You win!")

elif (choice == "0" and computer_choice == "1") or (choice == "1" and computer_choice == "2") or (choice == "2" and computer_choice == "0"):
    print("You lose!")

elif (choice == "0" and computer_choice == "0") or (choice == "1" and computer_choice == "1") or (choice == "2" and computer_choice == "2"):
    print("It's a tie!")
