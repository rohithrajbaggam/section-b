"""
*     *
  *  *
    *
  *  *
*      *
"""

n = int(input())

for i in range(n):
    for j in range(n):
        # print(i, j, end = " ->  ")
        if i == j or  i+j == n-1:
            print("*", end=" ")
        # elif i+j == n-1:
        #     print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

