text=input("enter the text")

vowels = "aeiou"

v_count = 0

c_count = 0

for ch in text:
    
    if ch in vowels:

        v_count+= 1
    else:
        c_count+= 1

print("v_count",v_count)        

print("c_count",c_count)



  
