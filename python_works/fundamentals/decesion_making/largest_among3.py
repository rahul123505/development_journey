num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))

if num1>num2 and num1>num3:

    # here i check if num1 is greater than num 2 and also check the num1 is graeter than num3 then num1 is greater
    print(num1," is greater")

# then i compare num2 is greater than num1 and num2 is greater than num3 then print num2 is greater
elif num2>num1 and num2>num3:
    print(num2," is greater") 

# here the num 1 and num 2 is not greater than num3 so it prints num3 is greater
else:
    print(num3,"is greater")       