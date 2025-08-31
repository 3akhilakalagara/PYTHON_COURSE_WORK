# a class can have multiple instances


class Student:
    #instance variables (can be accessed by class name or obj name)
    name = "xyz"
    branch = "cse"
    def read(self): #self is an implicit reference
        print("reading")
    def write(self):
        rno = 234 #local variables
        print(rno)
        print("instance variable=",self.branch)
        print("writing")

obj = Student()
obj.read()
obj.write()
print(obj.name) 