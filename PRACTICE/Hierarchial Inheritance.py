#(ONE TO MANY) HIERARCHIAL  INHERITANCE
class Status:
    def uploadImage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to status")

class StatusV1(Status):
    def addCaption(self,text):
        self.caption = text
        print(f"'{self.caption}' is added to your status")
        
class StatusV2(Status):
    def like(self):
        print(f"you can like the status")


obj = Status()
obj.uploadImage("picture.png")

obj1 = StatusV1()
obj1.uploadImage("RohitSharma.png")
obj1.addCaption("Captain")


obj2 = StatusV2()
obj2.uploadImage("Rohit.png")
obj2.like()