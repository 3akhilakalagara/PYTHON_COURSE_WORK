#A
n=int(input("enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or j==0 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
enter size:5
* * * * * 
*       * 
* * * * * 
*       * 
*       *
"""

#B
n=int(input("enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or j==0 or i==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
enter size:5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * *
"""

#C
n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
* * * * * 
*         
*         
*         
* * * * *
"""

#E

n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
* * * * * 
*         
* * * * * 
*         
* * * * *
"""



#F
   
n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
* * * * * 
*         
* * * * * 
*         
*
"""

#H

n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n//2 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
*       * 
*       * 
* * * * * 
*       * 
*       *
"""

#I

n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
* * * * * 
    *     
    *     
    *     
* * * * *
"""

#J

n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2 or (i == n - 1 and j <= n // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
Enter size: 5
* * * * * 
    *     
    *     
    *     
* * *
"""

















































































