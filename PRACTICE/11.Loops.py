# FOR LOOP
"""for var in seq(list/tuple/set/dict/str/range(start,stop)):
  block of code"""

#iterating list
l = [1,2,3,4,5]
for i in l:
  print(i)

#iterating tuple

t = (1,2,3,4,5)
for i in t:
  print(i)

#iterating set

s = {1,2,3,4,5}
for i in s:
  print(i)

#itearting dictionary
d = {"a":1, "b":2, "c":3, "d":4, "e":5}
for i in d.keys(): #for i in d:
  print(i)

d = {"a":1, "b":2, "c":3, "d":4, "e":5}
for i in d:
  print(i,d[i])

#values() return only values
d = {"a":1, "b":2, "c":3, "d":4, "e":5}
for i in d.values():
  print(i)

#items() return the dictionary(key:value)
d = {"a":1, "b":2, "c":3, "d":4, "e":5}
for i in d.items():
  print(i)

#iterating string
s = "Hyderabad"
for i in s:
  print(i)

#range

for i in range(0,11):
  print(i)

for i in range(2,10):
  print(i)

for i in range(2,20,2):
  print(i)

for i in range(6,2,-1):
  print(i)

for i in range(30,20,-2):
  print(i)

s = "hyderabad"
l = len(s)
for i in range(l):
  print(i,s[i])

l = [1,2,3,4,5,6,7,8]
for i in range(len(l)):
  print(i,l[i])

t = (1,2,3,4,5,6,7,8)
for i in range(len(t)):
  print(i,t[i])

#A dictionary in Python has no numeric index like a list, but it’s still an iterable.
#enumerate() just adds an index counter to whatever iterable you give it.

d = {"a":1, "b":2, "c":3, "d":4, "e":5}
for ind,i in enumerate(d):
  print(ind,i,d[i])

for i in range(1,10):
  if i==5:
    break
  print(i)

for i in range(1,10):
  if i==5:
    continue
  print(i)

for i in range(1,10):
  if i%2==0:
    continue
  print(i)

for i in range(10):
  if i == 6:
    break
  print(i)
else:
  print("end")

for i in range(10):
  if i == 6:
    continue
  print(i)
else:
  print("end")

#WHILE LOOP

"""
intialize value
while con:
  increament/decreament value

while True:
  if cond:
    break

"""

i = 1
while i<=10:
  print(i)
  i = i+1

j = 10
while j>=1:
  print(i)
  j = j-1

l=[1,2,3,4,5,6,1,2,3,4,1,26,4,3,2,1,6,3,2,1,5,3,2,1,4,1,2,5,6]
while 1 in l:
  l.remove(1)

print(l)

l=[2,3,4,5,6,2,3,4,26,4,3,2,6,3,2,5,3,2,4,2,5,6]

while 1 in l:
  l.remove(1)

print(l)

l=[1,2,3,4,5,6,1,2,3,4,1,26,4,3,2,1,6,3,2,1,5,3,2,1,4,1,2,5,6]

n = len(l)
ind = 0
while ind<n:
  print(l[ind])
  ind += 1

s = "while loop"
ind = 0
n = len(s)
while ind<n:
  print(s[ind])
  ind +=1

d = {"a":1, "b":2, "c":3, "d":4, "e":5}
k = tuple(d.keys())
i = 0
while i < len(k):
  print(k[i],d[k[i]])
  i=i+1
print(k)

t = ("a","b","c","d")
ind = 0
n = len(t)
while ind<n:
  print(t[ind])
  ind+=1