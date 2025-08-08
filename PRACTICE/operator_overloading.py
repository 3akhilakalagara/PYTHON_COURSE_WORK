class number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n+other.n 
    def __sub__(self,other):
        return self.n-other.n 
    def __mul__(self,other):
        return self.n*other.n
    def __str__(self): #used to print the object
        return f"{self.n}"

num1 = number(10)
num2 = number(20)

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1)