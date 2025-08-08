#(many TO one) HIERARCHIAL  INHERITANCE
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
        
class StatusV3(StatusV1,StatusV2):
    def addmusic(self,music):
        self.music = music
        print(f"{self.music}.. added to your status")
        
class StatusV4(StatusV3):
    def videolength(self,video):
        self.video = video
        print(f"{self.video} is uploaded to your status")


obj = Status()
obj.uploadImage("picture.png")

obj1 = StatusV1()
obj1.uploadImage("RohitSharma.png")
obj1.addCaption("Captain")


obj2 = StatusV2()
obj2.uploadImage("Rohit.png")
obj2.like()


obj3 = StatusV3()
obj3.uploadImage("War2.png")
obj3.addCaption("NTR")
obj3.addmusic("war2-teaser.mp3")
obj3.like()


obj4 = StatusV4()
obj4.uploadImage("War.png")
obj4.addCaption("Hrihtik Roshan")
obj4.like()
obj4.addmusic("war-bgm.mp3")
obj4.videolength("teaser.mp4")