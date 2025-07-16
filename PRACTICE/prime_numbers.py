#check num is prime or not
fact = 0
n = int(input("Enter a num:"))
for i in range(2, n+1):
    if n%i==0:
        fact+=1
if fact==1:
        print(f"{n} is prime number\nFactor count={fact}")
else:
    print(f"{n} is not prime number\nFactor count={fact}")
        
"""
Enter a num:21
21 is not prime number
Factor count=3
"""

#remove the 1 and factor itself of a num
fact = 0
n = int(input("Enter a num:"))
for i in range(2, (n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
        print(f"{n} is prime number\nFactor count={fact}")
else:
    print(f"{n} is not prime number\nFactor count={fact}")

"""
Enter a num:45
45 is not prime number
Factor count=4
"""
