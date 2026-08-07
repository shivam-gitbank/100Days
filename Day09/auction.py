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
    # how i solved the case my way this works as well 
    # bids = []
    # for i in data:
    #     bids.append(data[i])
    # max_bid = max(bids)
    # for j in data:
    #     if data[j] == max_bid:
    #         bname = j
    # return bname,max_bid

    max_name = max(data, key = data.get) # max func to work on key
    max_bid = max(data.values()) # max value in dict
    #max_bid = data[max_name] - got the key so printed it out by accessing via name
    return max_name, max_bid

oth_bidd = True
while oth_bidd != False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    other_bidder = input("are there any other bidders? Type 'yes' or 'no - ").lower()
    if other_bidder == 'yes':
        print("\033[H\033[2J", end="")
        BIDDERS[name] = bid # assignment operator is used to assign the key - name to the value- bid in dic BIDDERS
        oth_bidd = True
    else:
        BIDDERS[name] = bid # edge case - missing bid 
        bid_name, bid_max = highest_bid(BIDDERS)
        oth_bidd = False

print(f"the bid closes now - highest bid is of ${bid_max} and is won by {bid_name}")
