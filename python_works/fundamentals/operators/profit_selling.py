purchase_price = int(input("enter the price ot the product"))

profit_percentage = int(input("enter the profit percentage in "))

GST = 8

profit = profit_percentage/100 * purchase_price

selling_price = purchase_price+profit

gst_amount = (GST/100)*selling_price

total_amount = selling_price + gst_amount

print("the total amount=",total_amount)
