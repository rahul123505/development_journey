age = int(input("enter the age"))
if age>=0 and age<=12:

    print("child")

elif age>=13 and age<=19:

    print("teen")

elif age>=20 and age<=59:

    print("adult")  
    
elif age>=60:
    print("senior")

else:
    print("invalid age")    


