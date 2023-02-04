string = "a1b2c3d4e5f"

# string.is
num, alpha = "", ""
for  i in string:
    # print(i, i.isdigit())
    if i.isdigit():
        num += i 
    else:
        alpha += i 
    
print(num, alpha)
# string type casting to int
number = int(num)
print(type(num),number, type(number)) 

