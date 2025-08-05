#1
def cal(w,h):
  return w/h*h
w = float(input())
h = float(input())
print(cal(w,h))

#2
def f(*numbers):
  n=[]
  for i in numbers:
    if i%2==0:
      n.append(i)
  return n
print(f(1,2,3,4,5,6,8,10))

#3
def m(n):
  l =[]
  for i in range(1,11):
    a = n*i
    l.append(a)
  return l
n = int(input())
print(m(n))

#4
def anagram(str1, str2):
  return sorted(str1) == sorted(str2)

str1 = input()
str2 = input()
print(anagram(str1, str2))

#5
def w(text):
  freq = {}
  for w in text.split():
    freq[w] = freq.get(w, 0) + 1
  return freq
text = input()
print(w(text))

#8
def m(fn,ln,d):
  f=fn.lower()
  l=ln.lower()
  do=d.lower()
  return f"{f}.{l}@{do}.com"
fn = input()
ln = input()
d = input()
print(m(fn,ln,d))

#9
def f(n):
  a = []
  for i in range(1, n+1):
    if n%i==0:
      a.append(i)
  return a
n = int(input())
print(f(n))

#10
def f(i,q,p):
  total = q*p
  return f"{i} x {q} @ rs{p} = rs{total}"
i = input()
q = int(input())
p = int(input())
print(f(i,q,p))