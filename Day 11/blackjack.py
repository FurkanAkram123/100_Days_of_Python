import ASCII_Art
import random as rand
import os

cards = [11,10,10,10,10,9,8,7,6,5,4,3,2,]

def draw (card_set):
    card_set.append(rand.choice(cards))
    return card_set

def winner(player, dealer):

    """This function decides weather the use won or not"""

    if calculate(player) > 21 and len(player) > 2:
        print (ASCII_Art.lose)  

    elif (calculate(player) == 21 and len(player) == 2) or calculate(dealer) > 17 or (21< calculate(player) > calculate(dealer)):
        print (ASCII_Art.win)
   
    elif calculate(player) == calculate(dealer):
        print (ASCII_Art.draw)

    else:
        print (ASCII_Art.lose)
        return False

def calculate (card_set):

    """This function take's a list of cards and returns the sume"""
    if len(card_set) == 2 and sum(card_set) == 21:
        return 0
    if len(card_set) > 2 and sum(card_set) > 21:
        #replace the 11 with a 1 if sum is greater than 21
        card_set = [1 if x == 11 else x for x in card_set]
    return sum(card_set)

def show_score(player_cards, dealer_cards):
    winner(player_cards, dealer_cards)
    print (f"Dealers Cards: {dealer_cards}, Dealer's score: {calculate(dealer_cards)}")

def play_blackjack():

    print (ASCII_Art.logo)
    #start with an empty hand
    dealer_cards = []
    player_cards = []

    #first card for player & the dealer
    player_cards = draw(player_cards)
    dealer_cards = draw(dealer_cards)
    print (f"Your cards: {player_cards}, Your current score: {calculate(player_cards)}")
    print (f"The dealer's first card: {dealer_cards[0]}")
    
    while True:

        #Player's Choice - draw or keep
        if (input("Do you wish to draw another card? Type 'y' for yes or 'n' for no: ") == "y"):
            player_cards = draw(player_cards)
            dealer_cards = draw(dealer_cards)
            print (f"Your cards: {player_cards}, current score: {calculate(player_cards)}")
            print (f"The dealer's first card: {dealer_cards[0]}")

            #check the score
            if (calculate(player_cards) > 21 or calculate(dealer_cards) >=17):
                show_score(player_cards, dealer_cards)
                break
            elif calculate(player_cards) == 0:
                show_score(player_cards, dealer_cards)
                break
        elif len(player_cards) > 1:
            show_score(player_cards, dealer_cards)
            break

while True:
    
    if (input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ")) == "y":

        #clear the screen if player wants to play again
        os.system('cls')
        play_blackjack()
    else:
        break
