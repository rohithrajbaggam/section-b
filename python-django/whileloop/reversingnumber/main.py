n = int(input())
_sum = 0
temp = n 
while n > 0:
    rem = n%10 
    _sum = _sum*10 + rem 
    # print(rem)
    n = int(n/10) 

if _sum == temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")




