import random
import urllib.request
import tweepy
from tweepy import OAuthHandler
import numpy
import io
from google.cloud import vision
from google.cloud.vision import types
import os
import cv2
#import matplotlib.pyplot as plt

## variable about keys and tokens
consumer_key = 'input your consumer key'
consumer_secret = 'input your consumer secret'
access_token = 'input your access token'
access_token_secret = 'input your access token secret'


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="input the path you save the google vision key json file"

## get current path and make a folder
folder = os.getcwd()+"/images_and_video"

if not os.path.exists(folder):
    os.makedirs(folder)
 

def download_image(url_list):
	x = 0
	for item in url_list:
		# /Users/wang/Desktop/twitterProject/images/ <-- this part depends on which path to save the image
		filename = folder+'/%s.jpg' % x
		urllib.request.urlretrieve(item,filename)
		x+=1


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def getInfo():
	## number of tweets
	global tweetNum 
	tweetNum= int(input("please input the number of tweets you want to search: "))
	## ID of tweet account
	global tweetID 
	tweetID= str(input("please input the ID of tweet account: "))

def mainfunction():
	try:
		tweets = api.user_timeline(id = tweetID, count = tweetNum)
	except Exception:
		print('cannot find the user,please enter the right ID name')
		begin()
	else:
		image_url_list = []
		for status in tweets:
		    
			for media in status.entities.get('media',[]):
		        
				image_url_list.append(media.get("media_url"))

			## download images
		download_image(image_url_list)
		# check whether there are images inside the folder
		path = folder+'/'
		try:
			if(len(os.listdir(path)) == 0):
				raise Exception
		except Exception:
			print('No image please choose another user ID')
			begin()
		else:

			# Instantiates a client
			client = vision.ImageAnnotatorClient()
			def getLabel(file_name):
			# Loads the image into memory
			    with io.open(file_name, 'rb') as image_file:
			        content = image_file.read()

			    image = types.Image(content=content)

			# Performs label detection on the image file
			    response = client.label_detection(image=image)
			    labels = response.label_annotations
			    label_sum = []
			    for label in labels:
			       label_sum.append(label.description)
			       print(label.description)
			    return label_sum



			filePath = folder+'/'
			for file in os.listdir(filePath):
				if file.endswith(".jpg"):
					filename = filePath + file
					
			## Get labels:
					try:
						labels = getLabel(filename)
					except Exception:
						print("Error, please give the right filename")
					# use the default (fond) tff
					else:
						font=cv2.FONT_HERSHEY_SIMPLEX 
			 	
						im = cv2.imread(filename)

						i = 100
						for label in labels:
						# # 2 means font size，（50,i）is initial place，(69,0,255) is color of font，2 is font weight
							im=cv2.putText(im,label,(60,i),font,2,(69,0,255),3)
							i = i+60

						cv2.imwrite(filename,im)


			os.chdir(folder+'/')
			os.popen('ffmpeg -loop 1 -i %d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 0.5 -t 60 video.mp4','r',1)
	
def begin():
	try:
		getInfo()
	except Exception:
		print('error! please enter the right number or ID')
		begin()
	else:
		mainfunction()

begin()
