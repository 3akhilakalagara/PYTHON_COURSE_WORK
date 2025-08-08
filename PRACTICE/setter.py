class Instagram:
    def __init__(self,username,bio,acc_status=False):
        self.username = username
        self._bio = bio
        self.__acc_status = acc_status
    
    def get_acc_status(self): #getter method
            return self.__acc_status
    def set_acc_status(self,status): #setter method
            self.__acc_status = status
    
    @property
    def bio(self):
        return self._bio #protected variable
    @bio.setter
    def bio(self,new):
        self._bio = new

obj = Instagram("akhila","ntr",False)

print(obj.username)#public

print(obj.get_acc_status())#private

print(obj.bio)#protected
    