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
    print(f"the bid closes now - highest bid is of ${max_bid} and is won by {max_name}")

oth_bidd = True
while oth_bidd != False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    BIDDERS[name] = bid
    other_bidder = input("are there any other bidders? Type 'yes' or 'no - ").lower()
    if other_bidder == 'yes':
        continue
    else:
        oth_bidd = False
        highest_bid(BIDDERS)
        


