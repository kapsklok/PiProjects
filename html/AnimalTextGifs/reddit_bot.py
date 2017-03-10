import praw
import config
import time
import os

def bot_login() :
	print "Logging in..."
	r = praw.Reddit(client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "treburichet's dog comment test")
	print "Not logged in"
	return r

def run_bot(r, saved_posts):
	print "obtaining top " + repr(config.lim) + " posts of the day from " + config.sub
	for submission in r.subreddit(config.sub).top('day', limit=config.lim):
		line = "<a href=\"{}\" target=\"content\">{}</a>".format(submission.url, submission.title)
		#line = "<img src=\"{}\" alt=\"{}\" />".format(submission.url, submission.title)
		if line not in saved_posts:
			print submission.title + ", " + submission.url
			with open("posts.txt", "a") as f:
				f.write(line + "\n")
				saved_posts.append(line)
				#print line
			
def get_saved_posts():
	if not os.path.isfile("posts.txt"):
		saved_posts = []
	else:
		with open("posts.txt", "r") as f:
			saved_posts = f.read()
			saved_posts = saved_posts.split("\n")
			saved_posts = filter(None, saved_posts)
			#print saved_posts
	
	return saved_posts

r = bot_login()
saved_posts = get_saved_posts()

while True:
	run_bot(r, saved_posts)
	print "sleeping for 10s"
	time.sleep(10)

