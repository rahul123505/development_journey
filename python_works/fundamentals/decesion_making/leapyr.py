year=int(input("enter the year"))

if (year%4==0 and year%100!=0) or year%400==0: #if a year is divisible by 4 and not divisible by 100 is a leapyr. or the year is divisible by 400 is a leap year

    print(year,"is leapyear")

else:
    print(year,"is not leapyear")    