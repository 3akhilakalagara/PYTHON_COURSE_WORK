class normalUser:
    def playvideo(self,name):
        print(f"{name} is playing the video with:\n1.Normal Quality\n2.Ads run\n3.No bckg play\n4.limited downloads\n5.music with ads\n")
    
class premiumUser:
    def playvideo(self,name):
        print(f"{name} is playing the video with:\n1.High Quality\n2.No Ads\n3.Bckg play\n4.Unlimited downloads\n5.music without ads\n")
        
def play_video(user,username):
    user.playvideo(username)
        

a = normalUser()
b = premiumUser()
c = normalUser()
d = premiumUser()
e = normalUser()


play_video(a,"akhila")
play_video(b,"sree")
play_video(c,"nani")
play_video(d,"gk")
play_video(e,"maha")