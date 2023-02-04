n = int(input())
count = 0
for i in range(1, n):
    if n%i==0:
        count+=1
if count==1:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

