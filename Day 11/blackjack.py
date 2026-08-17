import ASCII_Art
import random as rand

print (ASCII_Art.logo)
cards = [11,10,9,8,7,6,5,4,3,2,1]

dealer_cards = []
player_cards = []

def draw ():
    return rand.choice(cards)

def winner():
    if sum(player_cards) > 21:
        print (ASCII_Art.lose)  
        return False
    elif sum(dealer_cards) > 21:
        print (ASCII_Art.win)
        return True
    elif sum(player_cards) == sum(dealer_cards):
        print (ASCII_Art.draw)
        return None
    elif sum(player_cards) > sum(dealer_cards):
        print (ASCII_Art.win)
        return True
    else:
        print (ASCII_Art.lose)
        return False

if (input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y"):

    while True:
        dealer_cards.append(draw())
        player_cards.append(draw())
        print (f"Your cards: {player_cards}, current score: {sum(player_cards)}")

        if (sum(player_cards) > 21 or input("Do you wish to draw another card? Type 'y' for yes or 'n' for no: ") == "n"):
            winner()
            print (f"Dealers Cards: {dealer_cards}, current score: {sum(dealer_cards)}")
            break

  
                
            
        
