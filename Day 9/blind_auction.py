from  ASCII_Art import Auction

#print the ASCII art
print (Auction[0])

#create a dictionary to store the bidders and their bids
bidder_list = {}

print ("\n")
print ("Hello, Welcome to the Blind Auction!")
input ("Press Enter to continue...")

def max_bid (bidder_list):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidder_list:
        if bidder_list[bidder] > highest_bid:
            highest_bid = bidder_list[bidder]
            highest_bidder = bidder

    return (f"The highest bid is: ${highest_bid} by {highest_bidder}")

while True:
    #ask for the bidder's name and bid
    bidder = input("Whats your name? ")
    bidder_list[bidder] = int(input("Whats your bid? $"))
    print ("\n")

    #check to see if there are any other bidders, if not print the highest bid and break the loop
    if (input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no"):
        print ("\n") 
        print (max_bid(bidder_list))
        break

