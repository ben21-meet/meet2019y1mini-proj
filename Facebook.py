users = []
posts = []
reciver_list = []

Email = input("Email - ")
Password = input("Password - ")
if Email == 'benchuk2004@gmail.com':
	print("Hey Benchuk2004")
if Password == 'roonaldinio12':
	print("You logged in!")

class User(object):
	def __init__(self,name,email,password,friend_list):
		friend_list = []
		posts = []
		self.name = name
		self.email = email
		self.password = password
		self.friend_list = friend_list
	def add_friend(self,email):
		self.friend_list.append(email)
		users.append(email)
		print((self.name) + " you added" + email + " as a friend")
	def remove_friend(self,email):
		self.friend_list.append(email)
		self.friend_list.remove(email)
		users.remove(email)
		print((self.name) + " you just removed" + email + " from your friend list")
	def post(self,text):
		posts.append(text)
		posts.append(self.posts)
		print((self.name) + " has posted" + text)
	def get_userInfo(self):
		print("Name:" + str(self.name) + "  Email:" + str(self.email) + "  Password:" + str(self.password) + "  Friends:" + str(self.friend_list) + "  Posts:" + str(self.posts))


class Post():
	def __init__(self,creator,image,video):
		self.creator = creator
		self.image = image
		self.video = video
	def post_image(self,text):
		posts.append(self.image)
		print((self.creator) + " You posted:" + text + (self.image))
	def post_video(self,text):
		posts.append(self.video)
		print((self.creator) + " You posted:" + text + (self.video))
	def remove_image(self):
		posts.append(self.image)
		posts.remove(self.image)
		print((self.creator) + " You removed this image: " + (self.image))
	def remove_video(self):
		posts.append(self.video)
		posts.append(self.video)
		print((self.creator) + " You removed this video: " + ( self.video))
	def get_post_listInfo(self):
		print("Image: " + str(self.image) + " |" + " Video: " + str(self.video) + " |" + " Creator: " + str(self.creator))


class Comment(Post):
	def __init__(self,like,gif,liked_posts,gif_list):
		liked_posts = []
		gif_list = []
		self.like = like
		self.gif = gif
		self.liked_posts = liked_posts
		self.gif_list = gif_list
	def comment(self,text):
		print("You commented:" + text)
	def _like_(self):
		self.liked_posts.append(self.like)
		print("You liked the post")
	def add_gif(self):
		self.gif_list.append(self.gif)
		print("You commented a gif:" + (self.gif))
	def remove_comment(self):
		print("You removed a comment")
	def _unlike_(self):
		self.liked_posts.append(self.like)
		self.liked_posts.remove(self.like) 
		print("You unliked the post")
	def delete_gif(self):
		self.gif_list.append(self.gif)
		self.gif_list.append(self.gif)
		print("You deleted this gif:" + (self.gif))


class Message(): 
	def __init__(self,sender,reciver):
		reciver_list = []
		self.sender = sender
		self.reciver = reciver
		reciver_list.append(users)
	def send_massage(self,text):
		users.append(self.reciver)
		reciver_list.append(self.reciver)
		print((self.sender) + " sended to:" + (self.reciver) +  text)
	def delete_massage(self):
		print((self.sender) + " You deleted you'r massage")
	def get_recivers_list(self):
		print((reciver_list))

while True:
	if 1==1:
		run.User()
		run.Post()
		run.Comment()
		run.Message()
				
	else:
		print("Imma heaad out")