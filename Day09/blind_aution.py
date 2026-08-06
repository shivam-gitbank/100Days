print("""
                          _________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ 
                      
                      """)


BIDDERS = {}
def highest_bid(data):
    max_name = max(data, key = data.get) # max func on key
    max_bid = max(data.values()) # max func on value
    return max_name, max_bid

oth_bidd = True
while oth_bidd != False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    other_bidder = input("are there any other bidders? Type 'yes' or 'no - ").lower()
    if other_bidder == 'yes':
        BIDDERS[name] = bid # assignment operator is used to assign the key - name to the value- bid in dic BIDDERS
        oth_bidd = True
    else:
        BIDDERS[name] = bid # edge case - missing bid 
        bid_name, bid_max = highest_bid(BIDDERS)
        oth_bidd = False

print(f"the bid closes now - highest bid is of ${bid_max} and is won by {bid_name}")
