from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"G'olib {winner}! Taklifi qilgan narxi: ${highest_bid}")



while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    bids[name] = price
    should_continue = input("Boshqa ishtirokchilar bormi? 'Ha' yoki 'Yo'q' deb yozing. ")
    if should_continue == "Yo'q":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "Ha":
        print("..../")

#Reklama huquqi asosida ;)
# pythontutor.com bironta ko`dga tusshunmay qolsangiz bu web appga kirib tushunib olishingiz mumkin...














