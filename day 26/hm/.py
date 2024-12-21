# დავალებაა 1

 #weight = int(input("enter your weight:"))
#height = int(input("enter your height:"))
  
#print(weight)
#print(height)


# დავალება 2

#yourbid = int(input("please enter how much you are bidding:"))
#yourbid = int(input("please enter how much you are bidding:"))
#maxbid = int(input("please enter your max bid:"))

#if maxbid >= 18000:
#    print("sold for:",maxbid)
def auction():
    highest_bid = 0
    winner = ""

    while True:
        name = input("Enter participant's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        try:
            bid = int(input(f"Enter {name}'s bid: "))
        except ValueError:
            print("Please enter a valid number for the bid.")
            continue

        if bid > highest_bid:
            highest_bid = bid
            winner = name
            print(f"Going once, going twice, current highest bid is {highest_bid} by {winner}!")
        else:
            print(f"{name}'s bid of {bid} is lower than the current highest bid of {highest_bid}.")

    print(f"Sold! The winner is {winner} with a bid of {highest_bid}!")

auction()



# დავალება 3






