#SINGLE INHERITANCE
class Status:
    def uploadImage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to status")

class StatusV1(Status):
    def addCaption(self,text):
        self.caption = text
        print(f"'{self.caption}' is added to your status")
        



obj = Status()
obj.uploadImage("picture.png")

obj1 = StatusV1()
obj1.uploadImage("RohitSharma.png")
obj1.addCaption("Captain")