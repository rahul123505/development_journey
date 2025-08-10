# read bill_total
# read number of dines
# read tip amount
# calculate invidual split

bill_total = int(input("enter the bill total"))

dines = int(input("enter the number of dines"))

tip_amount = int(input("enter the tip amount"))

total_amount = bill_total + tip_amount

individual_split = total_amount/dines

print("split",individual_split)
