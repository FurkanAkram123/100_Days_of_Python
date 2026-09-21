import os, subprocess
import math
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import Menu


#total amount of coins available
coins_available = 0
coins_quarter = 0
coins_dime = 0
coins_nickel = 0
coins_penny = 0


# Process the coins inserted by the user and return the total amount of money
def process_coins (user_pick):

    global coins_available, coins_quarter, coins_dime, coins_nickel, coins_penny

    #ask the user to insert coins
    print("Please insert coins. You can insert quarters, dimes, nickels, and pennies.")
    while True:
        try:
            quarters = int(input("Quarters?: "))
            if quarters*0.25 < Menu.MENU[user_pick]['cost']:
                dimes = int(input("Dimes?: "))
                if (quarters*0.25 + dimes*0.10) < Menu.MENU[user_pick]['cost']:
                    nickels = int(input("Nickels?: "))
                    if (quarters*0.25 + dimes*0.10 + nickels*0.05) < Menu.MENU[user_pick]['cost']:
                        pennies = int(input("Pennies?: "))
                        if (quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01) < Menu.MENU[user_pick]['cost']:
                            print("Sorry, that's not enough money. Money refunded.")
                            quarters, dimes, nickels, pennies = 0, 0, 0, 0
                            return 0, 0
                        
            #if the user inserted enough money, set the rest to 0
                    else: pennies = 0
                else: nickels, pennies = 0, 0
            else: dimes, nickels, pennies = 0, 0, 0

            #calculate the total amount of money inserted by the user and the change if any
            total_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            change = total_inserted - Menu.MENU[user_pick]['cost']

            # Add the coins inserted to the total amount of coins available in the machine
            for item in Menu.resources:
                if item == "money":
                    Menu.resources[item] += total_inserted
                elif item == "quarters":
                    Menu.resources[item] += quarters
                elif item == "dimes":
                    Menu.resources[item] += dimes
                elif item == "nickels":
                    Menu.resources[item] += nickels
                elif item == "pennies":
                    Menu.resources[item] += pennies
            break

        except ValueError:
            print("Please enter a valid number.")
            continue

    return total_inserted, change

def process_change(change):

    #loop through the coins available in the machine and return the change to the user
    while True:
        if change > 0:
            #Return quarters first, then dimes then nickels then pennies
            if Menu.resources['quarters'] > 0:
                quarters_to_return = math.floor(change / 0.25)
                if quarters_to_return > Menu.resources['quarters']:
                    quarters_to_return = Menu.resources['quarters']
                change -= quarters_to_return * 0.25
                Menu.resources['quarters'] -= quarters_to_return
            elif Menu.resources['dimes'] > 0:
                dimes_to_return = math.floor(change / 0.10)
                if dimes_to_return > Menu.resources['dimes']:
                    dimes_to_return = Menu.resources['dimes']
                change -= dimes_to_return * 0.10
                Menu.resources['dimes'] -= dimes_to_return
            elif Menu.resources['nickels'] > 0:
                nickels_to_return = math.floor(change / 0.05)
                if nickels_to_return > Menu.resources['nickels']:
                    nickels_to_return = Menu.resources['nickels']
                change -= nickels_to_return * 0.05
                Menu.resources['nickels'] -= nickels_to_return
            elif Menu.resources['pennies'] > 0:
                pennies_to_return = math.floor(change / 0.01)
                if pennies_to_return > Menu.resources['pennies']:
                    pennies_to_return = Menu.resources['pennies']
                change -= pennies_to_return * 0.01
                Menu.resources['pennies'] -= pennies_to_return

            print(f"Here is ${change:.2f} in change. You got {quarters_to_return} quarters, {dimes_to_return} dimes, {nickels_to_return} nickels, & {pennies_to_return} pennies.")
        else:
            print("No change to return.")

def confirm_drink(user_pick):
    #confirmation window popup
    root = tk.Tk()
    root.title("Confirmation popup")
    root.geometry("300x100")
    answer = askyesno(title="Confirmation", message=f"Are you sure you want to order a {user_pick}?")
    button = ttk.Button(root, text="Click to Confirm", command=confirm_drink)
    button.pack(expand=True)
    if answer:
        return True
    else:
        return False

# return the total amount of resources available in the machine
def make_report():
    print(f"Water: {Menu.resources['water']}ml")
    print(f"Milk: {Menu.resources['milk']}ml")
    print(f"Coffee: {Menu.resources['coffee']}g")
    print(f"Money: ${Menu.resources['money']:.1f}")
    print(f"Quarters: {Menu.resources['quarters']}")
    print(f"Dimes: {Menu.resources['dimes']}")
    print(f"Nickels: {Menu.resources['nickels']}")
    print(f"Pennies: {Menu.resources['pennies']}")

#check if the machine has enough resources to make the drink
def check_resources(drink):

    # loop through the menu ingredients and check if the machine has enough resources
    for item in Menu.MENU[drink]['ingredients']:
        if Menu.resources[item] < Menu.MENU[drink]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_drink(drink):
    # loop through the menu ingredients and deduct the resources used to make the drink
    for item in Menu.MENU[drink]['ingredients']:
        Menu.resources[item] -= Menu.MENU[drink]['ingredients'][item]
    print(f"Here is your {drink}. Enjoy!")

def main():
    global coins_available
    change = 0
    machine_on = True

    while machine_on:
        #ask the user what they would like to order
        user_pick = input("Welcome to the Coffee Machine! What would you like? (espresso/latte/cappuccino): ").lower()

        #confirm the choice with the user before continuing
        #if confirm_drink(user_pick):

        #check if the user wants a report of the machine's resources
        if user_pick == "report":
            make_report()

        #check if the user wants to turn off the machine
        elif user_pick == "off":
            machine_on = False

        #check if the user wants to order a drink from the menu
        elif user_pick in Menu.MENU:
            #check if the machine has enough resoources to make the drink
            if check_resources(user_pick):
                total_inserted, change = process_coins(user_pick)
                if total_inserted >= Menu.MENU[user_pick]['cost']:
                    process_change (change)
                    make_drink(user_pick)

    print("Thank you for using the Coffee Machine! Goodbye!")
       
if __name__ == "__main__":
    main()
    