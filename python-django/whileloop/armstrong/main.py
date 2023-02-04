_range = int(input())
for i in range(_range):
    n = i 
    temp = n 
    _sum = 0
    count = 0
    temp_n = n 
    length = 0 
    # length of n 
    while temp_n > 0:
        length+=1 
        temp_n = int(temp_n/10)

    # sum 
    while n > 0:
        rem = n%10 
        _sum += (rem**length )
        count += 1
        # print(rem)
        n = int(n/10) 
    # comparing 
    if temp == _sum:
        print(f"{temp} is armstrong")
    # else:
    #     print(f"{temp} is not armstrong")






# n = int(input())
# temp = n 
# _sum = 0
# count = 0
# temp_n = n 
# length = 0 

# while temp_n > 0:
#     length+=1 
#     temp_n = int(temp_n/10)


# while n > 0:
#     rem = n%10 
#     _sum += (rem**length )
#     count += 1
#     # print(rem)
#     n = int(n/10) 

# if temp == _sum:
#     print(f"{temp} is armstrong")
# else:
#     print(f"{temp} is not armstrong")
# # print(count)



