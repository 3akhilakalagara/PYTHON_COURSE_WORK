#1

import math

def circle(radius):
  area = math.pi*radius*radius
  circumference = 2*math.pi*radius
  print('(%.2f,%.2f)'%(area, circumference))

circle(7)

#2

import random

def pick_random_team(members,team_size):
  print(random.choices(members,k=team_size))


pick_random_team(["A","B","C","D","E"], 3)

#3
temp = list(filter(lambda i:i>40,[35,42,39,45,41]))
print(temp)

#4

"""n=int(input())
for i in range(2,n//2+1):
  if n%i==0:
    print('not prime')
    break
else:
  print('prime')"""


#using recursion

def prime(n,i=2):
  if i == n//2+1:
    return True
  if n%i==0:
    return False
  return prime(n,i+1)

n = int(input())
if (prime(n,2)):
  print('prime')
else:
  print('not prime')

#5
def reverse_number(n):
    if n < 10:  # Base case: single digit
        return n
    digits = len(str(n)) - 1
    return (n % 10) * (10 ** digits) + reverse_number(n // 10)

# Input
n = int(input())
print(reverse_number(n))


#6
seq = ["cat","car","apple","banana"]
ch = "c"
letter = list(filter(lambda x:x.startswith(ch),seq))
print(letter)

#7

#8
l = ["Apple","apple","BANANA","banana","Cherry"]
s = {i.lower() for i in l}
print(s)

#lambda
up = set(map(lambda i:i.lower(),l))

#9

def countdown(n):
  for i in range(n,0,-1):
    yield i
values = countdown(3)
for value in values:
  print(value)

#10

def sumlist(l,i=0):
  sum= 0
  for i in l:
    if type(i) == int:
      sum += i
    else:
      sum += sumlist(i)
  return sum

sumlist([2,3,[3,[4,5,6]]])