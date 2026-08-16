from  ASCII_Art import Auction
import os

#print the ASCII art
print (Auction[0])

#create a dictionary to store the bidders and their bids
bidder_list = {}

print ("\n")
print ("Hello, Welcome to the Blind Auction!")
input ("Press Enter to continue...")

def max_bid (bidder_list):
    highest_bid = max(bidder_list.values())
    highest_bidder = max(bidder_list, key=bidder_list.get)

    return (f"The highest bid is: ${highest_bid} by {highest_bidder}")

while True:
    #ask for the bidder's name and bid
    bidder = input("Whats your name? ")
    bidder_list[bidder] = int(input("Whats your bid? $"))

    #clear the screen for the next bidder
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #check to see if there are any other bidders, if not print the highest bid and break the loop
    if (input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no"):
        print (max_bid(bidder_list))
        break
    

