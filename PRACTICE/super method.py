#SUPER METHOD(USED WHEN WE HAVE SAME METHODS)

class Instagram:
    def __init__(self,username):
        self.username = username
        self.post  = []
        print(f"{self.username.center(40,"-")}")
    
    def uploadPost(self,image):
        self.post.append(image)
        print(f"{image} is posted")   
    
class InstagramV1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio = bio
        print("bio is uploaded")
    def uploadPost(self,post,music):
        super().uploadPost(post)
        self.music = music
        print(f"{self.music} is uploaded")



obj = Instagram("chowdary__45")
obj.uploadPost("NTR.png")

obj1 = InstagramV1("chowdary__45","@jrntr")
obj1.uploadPost("NTR.png","Chuttamalle.mp3")