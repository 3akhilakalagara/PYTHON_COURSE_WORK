# Conditional Statements Practice

#1.Positive or Negative
a = int(input("Enter a number: "))
if a<0:
  print("-ve")
else:
  print("+ve")
  
"""
Enter a number: 76
+ve
"""

#2.Even or Odd
a = int(input("Enter a number: "))
if a%2 == 0:
  print(f"{a} is an even number")
else:
  print(f"{a} is an odd number")
  
"""
Enter a number: 3
3 is an odd number
"""

#3.Divisible by 5
a = int(input("Enter a number: "))
if a%5 == 0:
  print(f"{a} is divisible by 5")
else:
  print(f"{a} is not divisible by 5")
  
"""
Enter a number: 45
45 is divisible by 5
"""

#4.Divisible by 3 and 7
a = int(input("Enter a number: "))
if a%3==0 and a%7==0:
  print(f"{a} is divisible by both 3&7")
else:
  print(f"{a} is not divisible by both 3&7")

"""
Enter a number: 21
21 is divisible by both 3&7
"""

#5.Check for Leap Year
a = int(input("Enter a number: "))
if (a%4==0 and a%100!=0) or a%400==0:
  print(f"{a} is a leap year")
else:
  print(f"{a} is not a leap year")

"""
Enter a number: 2021
2021 is not a leap year
"""

#6.Check pass or fail
a = int(input("Enter marks: "))
if a>=35:
  print("pass")
else:
  print("fail")
  
"""
Enter marks: 45
pass
"""

#7.Check if number is 3-digit
a = input("Enter a number: ")
if len(a) == 3:
  print(f"{a} is a 3-digit number" )
else:
  print(f"{a} is not a 3-dgit number")

"""
Enter a number: 32
32 is not a 3-dgit number
"""

#8.Check if character is vowel or consonant
x = input("Enter a character : ")
y = ["a", "e", "i", "o", 'u']
if x.lower() in y:
  print(f"{x} is Vowel")
else:
  print(f"{x} is consonant")

"""
Enter a character : k
k is consonant
"""

#9.Check greatest of two numbers
a = int(input("Enter a number: "))
b = int(input("Enter b number:"))
if a>b:
  print(f"{a} is greater than {b}")
else:
  print(f"{b} is greater than {a}")

"""
Enter a number: 78
Enter b number:54
78 is greater than 54
"""

#10.Check smallest of two numbers
a = int(input("Enter a number: "))
b = int(input("Enter b number:"))
if a<b:
  print(f"{a} is less than {b}")
else:
  print(f"{b} is less than {a}")

"""
Enter a number: 9
Enter b number:5
5 is less than 9
"""

#11.Check if number is zero
a = int(input("Enter a number:"))
if a==0:
  print(f"number is {a}")
else:
  print(f"number is not {a}")

"""
Enter a number:0
number is 0
"""

#12.Check if number is multiple of 10
a = int(input("Enter a number:"))
if a%10 == 0:
  print(f"{a} is multiple of 10")
else:
  print(f"{a} is not multiple of 10")

"""
Enter a number:45
45 is not multiple of 10
"""

#13.Check vote eligibility
a = int(input("Enter age:"))
if a>=18:
  print("eligible to vote")
else:
  print("not eligible to vote")

"""
Enter age:21
eligible to vote
"""

#14.Check if number is in range 1-100
a = int(input("enter a number:"))
b = range(1,100)
if a in b:
  print(f"{a} is in range")
else:
  print(f"{a} is not in range")

"""
enter a number:45
45 is in range
"""
#15.Check if number is square of another number
a = int(input("Enter a number:"))
b = int(input("Enter b number"))
if a == b**2:
  print(f"{a} is square of {b}")
else:
  print(f"{a} is not square of {b}")

"""
Enter a number:9
Enter b number10
9 is not square of 10
"""

#16.Check if two strings are equal
a = input("enter a str:")
b = input("enter b str:")
if a == b:
  print("strings are equal")
else:
  print("strings are not equal")

"""
enter a str:akhila
enter b str:sharma
strings are not equal
"""
#17.check if number is prime
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number")
elif num == 2 or num == 3 or num == 5 or num == 7:
    print(f"{num} is a Prime number")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a Prime number")

"""
Enter a number: 32
32 is not a prime number
"""
#18.Check if number is +ve and even
a = int(input("Enter a number: "))
if a>0 and a%2==0:
  print(f"{a} is +ve and even")
else:
  print(f"{a} is not +ve and even")

"""
Enter a number: -5
-5 is not +ve and even
"""

#19.Check if string is in uppercase
a = input("Enter a str: ")
if a.isupper():
  print(f"{a} is in uppercase")
else:
  print(f"{a} is not in uppercase")

"""
Enter a str: a
a is not in uppercase
"""
#20.Check if string is in lowercase
temp = int(input("Enter a temp:"))
if temp>30:
  print("it's hot")
else:
  print("it's not hot")

"""
Enter a temp:98
it's hot
"""