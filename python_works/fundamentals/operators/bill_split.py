bill_amount = int(input("enter the bill amount"))

dines_count = int(input("enter the dines count"))

tip = 12/100*bill_amount

gst_amount = 8/100*bill_amount

total_amount = bill_amount+gst_amount+tip

split_amount = total_amount/dines_count

print("total amount is=",total_amount,"splitamount=",split_amount)

