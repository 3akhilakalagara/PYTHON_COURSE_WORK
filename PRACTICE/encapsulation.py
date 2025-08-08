class Details:
    def __init__(self,name,mail,pwd):
        self.name = name #public
        self._mail = mail #protected
        self.__pwd = pwd #private
        
    def getpassword(self): #getter method
            return self.__pwd
    def setpassword(self,new_pwd): #setter method
            self.__pwd = new_pwd
            
obj = Details("Akhila","akhila@gmail.com","akhila@45")


#accessing and modifying public variable
print(obj.name)
obj.name = "Sree"
print(obj.name)


#accessing and modifying protected variable
print(obj._mail)
obj._mail = "akhila45@gmail.com"
print(obj._mail)



#accessing and modifying private variable
print(obj.getpassword())
obj.setpassword("Akhila45")
print(obj.getpassword())

        