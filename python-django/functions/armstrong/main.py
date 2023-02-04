


def findLength(n):
    count = 0
    while n > 0:
        count+=1 
        n = int(n/10)
    return count 

def findSum(n, length):
    _sum = 0
    while n > 0:
        rem = n%10 
        _sum += (rem**length)
        n = int(n/10)
    return _sum 

def isArmstrong(n, _sum):
    if n == _sum:
        return True 
    else:
        return False 

def armstrongInCertainRange(_range):
    for i in range(_range):
        n = i 
        length = findLength(n) 
        _sum = findSum(n, length)
        if isArmstrong(n, _sum):
            print(i)

# _range = int(input())
# armstrongInCertainRange(_range)


# print(findSum(n, length))
