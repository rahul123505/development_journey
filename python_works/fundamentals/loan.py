P = int(input("enter the loan amount"))

tenur = int(input("enter the tenur year"))

rate_interest = int(input("enter the rate of interest"))

R = rate_interest/12/100 #monthly interest rate(calculated as the anuval interest rate divided by 12 and then divided by 100)

tenur_month = tenur*12#loan tenur in monthly


emi=(P*R*(1+R)**tenur_month)/((1+R)**tenur_month-1)

print("emi =",emi)

total_amount = emi*tenur_month

total_interest = total_amount-P

print("total aount want to pay",total_amount)

print("total interest is",total_interest)

