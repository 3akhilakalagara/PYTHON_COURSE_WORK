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
names = input("Enter names:")
unique = set(map(str.strip, names.split(',')))
print(sorted(unique))

"""
Enter names:bmw,audi,benz,innova,jaguar,benz,porsche,audi
['audi', 'benz', 'bmw', 'innova', 'jaguar', 'porsche']
"""

#7. STUDNET MARKS RECORD (DICTIONARY OPERATIONS)
q = int(input("Enter number of students: "))
stds = input("Enter student name and marks: ").split(" ")
dict_ = dict(zip(stds[0::2], map(int, stds[1::2])))
maximum = max(dict_, key=dict_.get)
print(maximum)



    