from  ASCII_Art import Auction

#print the ASCII art
print (Auction[0])

#create a dictionary to store the bidders and their bids
bidder_list = {}
highest_bid = 0
highest_bidder = ""

print ("\n")
print ("Hello, Welcome to the Blind Auction!")
input ("Press Enter to continue...")

while True:
    #ask for the bidder's name and bid
    bidder = input("Whats your name? ")
    bidder_list[bidder] = int(input("Whats your bid? $"))
    print ("\n")

    #check to see if the current bid is higher than the highest bid
    if highest_bid < bidder_list[bidder]:
        highest_bid = bidder_list[bidder]
        highest_bidder = bidder

    #check to see if there are any other bidders, if not print the highest bid and break the loop
    if (input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no"):
        print ("\n") 
        print (f"highest bid is: ${highest_bid} by {highest_bidder}")
        break


