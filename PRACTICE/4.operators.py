#1.Arithmetic Operators
a=45
b=5
print("addition:", a+b) #addition: 50
print("subtraction:", a-b) #subtraction: 40
print("multiplication:", a*b) #multiplication: 225
print("division:", a/b) #division: 9.0
print("floor division:", a//b) #floor division: 9
print("modulus:", a%b) #modulus: 0
print("exponential:", a**b) #exponential: 184528125

#2.Comparison Operators
x=20
y=30
print("equal to:", x==y) #equal to: False
print("not equal to:", x!=y) #not equal to: True
print("greater than:", x>y) #greater than: False
print("less than:", x<y) #less than: True
print("greater than or equal:", x>=y) #greater than or equal: False
print("less than or equal:", x<=y) #less than or equal: True

#3.Assignment Operators
"""
var=var(Ope)((val)
k=k+10
var(ope)=val
k+=10
"""
k=10
print("assign:", k) #assign: 10
k+=10
print("add&assign:", k) #add&assign: 20
k-=10
print("sub&assign:", k) #sub&assign: 10
k*=10
print("multiply&assign:", k) #multiply&assign: 100
k/=10
print("divide&assign:", k) #divide&assign: 10.0
k//=10
print("floordivide&assign:", k) #floordivide&assign: 1.0
k%=10
print("modulus&assign:", k) #modulus&assign: 1.0
k**=10
print("exponentiate&assign:", k) #exponentiate&assign: 1.0

#4.Logical Operators
"""
AND GATE = true only if all the stmts are ture
OR GATE = true if any one of the stmt is true
NOT GATE = returns reverse of the stmt
"""

m=20
n=30
print("AND GATE:", m<n and n>m) #AND GATE: True
print("OR GATE:", m<n or n>m) #OR GATE: True
print("NOT GATE:", not m<n) #NOT GATE: False

#5.Membership Operators
names=["rohit sharma","MI","T20","Captain"]
print("in result:", "MI" in names)#in result: True
print("not in result:", "India" not in names) #not in result: True

#6.Identity Operators
a=[1,2,3,4,5]
b=[1,2,3,4,5]
m=n #n is assigned to m

print("id(a):", id(a))# id(a): 2348072432576
print("id(b):", id(b))# id(b): 2348072326848
print("is result:", a is b)# is result: False
print("is not result:", a is not b)# is not result: True
print("is result:", m is n)# is result: True

#Bitwise Operators
'''
bitwise and - &
bitwise or - |
bitwise xor - ^
bitwise not - ~
left shift - <<
right shift - >>
'''
k=4
n=5
print("bitwise &:", k&n)# bitwise &: 4
print("bitwise |:", k|n)# bitwise |: 5
print("bitwise ^:", k^n)# bitwise ^: 1
print("bitwise ~:", ~k)# bitwise ~: -5
print("left shift:", k<<n)# left shift: 128
print("right shift:", k>>n)# right shift: 0



