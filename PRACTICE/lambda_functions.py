"""
lambda function:

lambda arguments:expression

used because it makes code shorter ans easy

"""

def evenodd(n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"
n = int(input())
print(evenodd(n))


#lambda function
iseven = lambda n: "even" if n%2==0 else "odd"
print(iseven(n))


#squares
def squares(n):
    return n*n
n = int(input())
print(squares(n))

sq=lambda n: n*n  """lambda function"""
print(sq(n))

#divide
def divide(a,b):
    return a/b
a = int(input())
b = int(input())

print(divide(a,b))

#lambda

div = lambda a,b: a/b
print(div(a,b))


#squares of list using lambda
def squares(l):
    for i in rnge(len(l)):
        l[i] = l[i] ** 2
    return l
l=[1,2,3,4,5]
print(squares(l))


squa=list(map(lambda i: i**2, l))"""lambda"""
print(squa)

#strings
l=["akhila","gk","maha","gayathri"]
sq=list(map(lambda i:i.title(),l))
print(sq)

#capitalize
l="python"
cap=list(map(lambda i:i.upper(),l))
print(cap)

#replce vowels
l="python"
v="aeiou"
vow=list(map(lambda i:"*" if i in v else i,l))
print(vow)

#filter(based on the condition filtering the data)
l=[1,2,3,4,5,6,7,8]
even=list(filter(lambda i:i%2==0,l))
print(even)


#remove zero's from the list
l=[1,0,0,0,0,0,0,0,0,0,0,0,2,3,4,5]
zero=list(filter(lambda i:i!=0,l))
print(zero)

#reduce(gives a single value)
from functools import reduce
num = [1,2,3,4,5] """or ["anme","tuy","yuhj"]"""
sum_ = reuce(lambda x, y: x*y, numbers)
print(sum_)



#dictionary
data={"mouse":True,"laptop":False,"phone":True,"charger":True}
d=list(filter(lambda i:data[i],data))#filters and gives triue values
print(d)

#name and marks
data ={"a":67,"B":49,"c":89}
d=dict(sorted(data.items(),key=lambda i:i[1],reverse=True))#key=i[0],asc=i[1]
print(d)



#list comprehensions
l=[i for i in range(1,11) if i%2==0]
print(l)

#set comprehension
l={i for i in range(1,11) if i%2==0}
print(l)

#dictiionary comprehension
k={i:i**2 for i in range(1,11)}
print(k)

l=["pen","mouse","bench","pencil"]
m=(i+1:l[i] for i in range(len(l)))
print(m)

#tuple
k=tuple(i for i in range(1,10))
print(k)

a="abcdefghijklmnoopqrstuvwxyz"
p={i:0 for i in a}
print(p)




























































