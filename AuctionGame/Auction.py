auction_participants = {}
continue_the_auction = True
maximum_bidder = ""
maximum_bid = 0

while continue_the_auction:
    name = input("Enter your name: ")
    amount = int(input("Enter amount: "))
    auction_participants[name] = amount
    any_more_participants = input("Are there any other participants? ").lower()
    if any_more_participants == "no":
        continue_the_auction = False

for keys in auction_participants:
    if auction_participants[keys] > maximum_bid:
        maximum_bidder = keys
        maximum_bid = auction_participants[keys]

print(maximum_bidder)
print(maximum_bid)