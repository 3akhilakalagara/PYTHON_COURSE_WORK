#1.THE BIRTHDAY FORMAT FIXER(STRING AND TYPE CONVERSION)

x = input("Enter date(dd-mm-yyyy):")
d, m, y = x.split('-')
d = int(d)
m = int(m)
y = int(y)
print(f"{y:04d}/{m:02d}/{d:02d}")

"""Enter date(dd-mm-yyyy):23-07-2013
2013/07/23
"""

#2. THE EVEN ODD GAME(CONDITIONAL STATEMENT)
x = int(input("Enter a number:"))
if x%2 == 0:
    print("Even Winner")
else:
    print("Odd Winner")

"""Enter a number:45
Odd Winner
"""

#3. VOWEL REPLACER BOT(STRING METHODS)
n = input("Enter a string:")
v = n.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
print(v)

"""
Enter a string:hello world
h*ll* w*rld
"""

#4. SHOPPING CART ANALYZER(LIST OPERATIONS)
l = list(map(float, input("Enter prices:").split(" ")))
print(f"Total:{sum(l)}")
print(f"MAX_value:{max(l)}")

"""Enter prices:21.09 1.05 100.98 45.65
Total:168.77
MAX_value:100.98
"""

#5. SECURE LOGIN SYSTEM
credentials = ("admin", "python123")
t = input("Enter username: ")
p = input("Enter password: ")
if t==credentials[0] and p==credentials[1]:
    print("Login Successful")
else:
    print("Access Denied")
    
"""
Enter username: admin
Enter password: oiuy
Access Denied
"""

#6. REMOVE DUPLICATES FROM SET(SET OPERATIONS)
n=set(input().split(","))
print(sorted(n))

"""
Enter names:bmw,audi,benz,innova,jaguar,benz,porsche,audi
['audi', 'benz', 'bmw', 'innova', 'jaguar', 'porsche']
"""

#7. STUDNET MARKS RECORD (DICTIONARY OPERATIONS)
n=int(input("Enter number of students: "))
data ={}
max_val = 0
res =""
for i in range(n):
    name,marks=input().split()
    marks=int(marks)
    if marks>max_val:
        res=name
    data[name] = marks
print(data)
print(res)

#8. REVERSE MY WORDS(STRING SLICING)
y=input("Enter a str:").split()
for i in y:
    print(i[::-1], end=" ")

#9. CLEAN MY LIST(LIST AND TYPE CONVERSION)
o=input()
o=o.replace("0","")
print(o.split())

#10. FREQUENCY COUNTER
g=input("Enter a string:")
r={}
for i in g:
    if i not in r and i != " ":
        r[i] = g.count(i)
print(r)

