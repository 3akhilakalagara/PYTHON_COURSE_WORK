class normalUser:
    def playvideo(self,name):
        print(f"{name} is playing the video with:\n1.Normal Quality\n2.Ads run\n3.No bckg play\n4.limited downloads\n5.music with ads\n")
    def likes(self):
        pass
    def comments(self):
        pass
    def description(self):
        pass
    def subscribe(self):
        pass
    
class premiumUser:
    def playvideo(self,name):
        print(f"{name} is playing the video with:\n1.High Quality\n2.No Ads\n3.Bckg play\n4.Unlimited downloads\n5.music without ads\n")
        

a = normalUser()
b = premiumUser()

a.playvideo("akhila")
b.playvideo("sree")