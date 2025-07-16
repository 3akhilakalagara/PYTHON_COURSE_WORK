#NESTED LOOPS(outer-loop(rows), inner-loop(column))

for row in range(5):
    for colu in range(5):
        print("*",end=" ")
    print()

"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
"""

for i in range(5):
    for j in range(5):
        print(i,end=" ")
    print()

"""
0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4
"""

for i in range(5):
    for j in range(5):
        print(j,end=" ")
    print()

"""
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4 
0 1 2 3 4
"""

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

"""
* 
* * 
* * * 
* * * * 
* * * * *
"""

for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()
"""
* * * * * 
* * * * 
* * * 
* * 
*
"""
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * *
"""

for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for k in range(5-i):
        print("*",end=" ")
    print()

"""
* * * * * 
  * * * * 
    * * * 
      * * 
        *
"""

n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
Enter size:10
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * *
"""

n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
Enter size:5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * *
"""

n=int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
* * * * * 
      *   
    *     
  *       
* * * * *
"""

n = int(input("Enter size:"))
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
"""
Enter size:5
*       * 
  *   *   
    *     
  *   *   
*       *
"""
















































































    












