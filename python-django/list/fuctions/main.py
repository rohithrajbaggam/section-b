

def sort(mylist):
    for i in range(len(mylist)):
        print(mylist)
        for j in range(len(mylist)):
            if mylist[i] < mylist[j]:
                # swap
                mylist[i], mylist[j] = mylist[j], mylist[i]


mylist = [2, 5, 1, 3 ,4]

# print(mylist)

sort(mylist)

print(mylist)














# def linearSearch(mylist, val):
#     for i in mylist:
#         if i == val: 
#             return True 
#     return False 


# mylist = [1, 2,3, 4, 5,1]

# print(linearSearch(mylist, 6))

# print(mylist.count(1))
# mylist.sort(reverse=True)
# print(mylist)


