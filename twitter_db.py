import random
import urllib
import tweepy
from tweepy import OAuthHandler
import numpy
import io
from google.cloud import vision
from google.cloud.vision import types
import os
import cv2
import matplotlib.pyplot as plt
import pymongo
import time
from random import choice
import mysql.connector
'''
	This program is designed for user to use the API to get the image and transfer them into videos.
	Besides basic functions, user can use this API to store information to the MySQL or Mongo DATABASES

'''

personal_use = False
test_mode = True

class twitter_API:

	def __init__(self,user):
		self.user = user

	def credential(self):
		# credential for tweepy
		self.consumer_key = '7W7HK7ltZH8PbyZVMLTpxMRFN'
		self.consumer_secret= 'BrMH5E3X5HnzhHlj3EAje0uMHikFx20NOzyQo9GDNzSuJCXpzq'
		self.access_token = '1037537164899352582-1KDZ4I4J3WOXbnmTPOEUUDkCwIoaR7'
		self.access_token_secret = 'hZeTG7X3uNfkUvzXn7oOEuXKe4R6ehybwyIMQOGwdHGVe'
		# credential for google API
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/wang/Desktop/MiniProject3/key.json"

	def preprocess(self): 
		# get current datatime
		datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
		self.datetime = datetime

		# get current path and make a folder to store the image
		folder = os.getcwd()+"/images_and_video/"+self.user+" "+str(datetime)

		if not os.path.exists(folder):
			os.makedirs(folder)

		self.folder = folder

	def download_image(self,url_list):
		'''
			This part is for downloading the images from tweets
		'''
		x = 0
		for item in url_list:
			filename = self.folder+'/%s.jpg' % x
			urllib.request.urlretrieve(item,filename)
			x+=1

	def getInfo(self):

		'''
			If for personal use, this part can get inputs from the user
			for the number of tweets and Accout ID 
		'''
		if personal_use:
			# number of tweets
			self.tweetNum= int(input("please input the number of tweets you want to search: "))

			# ID of tweet account
			self.tweetID= str(input("please input the ID of tweet account: "))
		'''
			This part is for the test.
			Automatically choosinng account ID and number 
		'''
		if test_mode:
			id_pool = ['NBA','lol','kobe','james','SLAMonline','NBAonTNT',
						'StephenCurry30','JHarden13','JLin7','HoustonRockets']
			number_pool = [20,25,35,30,40,45,50]
			self.tweetID = str(choice(id_pool))
			self.tweetNum = int(choice(number_pool))


	def getLabel(self,file_name):
		'''
			This part is for getting the label of images
		'''
		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = self.vision_client.label_detection(image=image)
		labels = response.label_annotations
		label_sum = []
		for label in labels:
			label_sum.append(label.description)
			# print(label.description)
		return label_sum

	def video(self):
		'''
			This part is for transferring the images with labels into video
		'''
		os.chdir(self.folder+'/')
		os.popen('ffmpeg -loop 1 -i %d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 0.5 -t 60 video.mp4','r',1)


	def mongodb(self):
		'''
			connect to the mongodb
		'''
		self.client = pymongo.MongoClient()
		self.mydb = self.client.twitter_mongo
		self.mycol = self.mydb.user

	def connect_mysql(self):
		'''
			connect to mysql 
		'''
		self.sqldb = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="12345678",
			database = "twitter_mysql"
			)
		self.mycursor = self.sqldb.cursor()

	def implement(self):
		# connect to the tweep api
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token,self.access_token_secret)
		api = tweepy.API(auth)
		print('............successfully connect to tweepy..............')
		label_list = []

		try:
			tweets = api.user_timeline(id = self.tweetID, count = self.tweetNum)
		except Exception:
			print('cannot find the user,please enter the right ID name')
			self.begin()
		else:
			image_url_list = []
			for status in tweets:
				for media in status.entities.get('media',[]):
					image_url_list.append(media.get("media_url"))

			self.image_url_list = image_url_list

			# download images
			self.download_image(image_url_list)
			path = self.folder+'/'
			try:
				if(len(os.listdir(path)) == 0):
					raise Exception
			except Exception:
				print('No image please choose another user ID')
				self.begin()
			else:
				# Instantiates a client
				self.vision_client = vision.ImageAnnotatorClient()
				filePath = self.folder+'/'

				for file in os.listdir(filePath):
					if file.endswith(".jpg"):
						filename = filePath + file

						# Get labels:
						try:
							labels = self.getLabel(filename)
							label_list.append(labels)

						except Exception:
							print("Error, please give the right filename")
						
						# use the default (fond) tff
						else:
							font=cv2.FONT_HERSHEY_SIMPLEX

							im = cv2.imread(filename)

							i = 100
							for label in labels:
								'''
								 2 means font size,(50,i)is initial place,
								 (69,0,255) is color of font,2 is font weight
								 '''
								im=cv2.putText(im,label,(60,i),font,1.,(69,0,255),2)
								i = i+50

							cv2.imwrite(filename,im)
				self.label_list = label_list

	def insert(self):

		# insert data into mongo
		user_dict = {}
		user_dict['username'] = self.user
		user_dict['searchID'] = str(self.tweetID)
		user_dict['serchNum'] = str(self.tweetNum)
		user_dict['datetime'] = self.datetime 
		user_dict['credential'] = [self.consumer_key, self.consumer_secret, 
									elf.access_token, self.access_token_secret],
		user_dict['url_list'] = self.image_url_list
		user_dict['label_list'] =  self.label_list
		x = self.mycol.insert_one(user_dict)

	
	def insert_mysql(self,id):
		# insert data into mysql
		sql1 ="INSERT INTO user (id,username) VALUES(%s,%s)"
		val1 = (id,self.user)
		try:
			self.mycursor.execute(sql1,val1)
			self.sqldb.commit()
		except:
			print('fail!!!!')
			self.sqldb.rollback()
<<<<<<< HEAD

		sql2 = '''INSERT INTO activity (username, searchID, searchNum, searchDate, imageNum)
				VALUES (%s,%s,%s,%s,%s)
				'''
		val2 = (self.user, str(self.tweetID), str(self.tweetNum), 
				self.datetime, str(len(self.image_url_list)))
=======
# 		self.mycursor.execute(sql1,val1)
# 		self.sqldb.commit()
		sql2 = '''INSERT INTO activity (username, searchID, searchNum, searchDate, imageNum)
				VALUES (%s,%s,%s,%s,%s)
				'''
		val2 = (self.user, str(self.tweetID), str(self.tweetNum), self.datetime, str(len(self.image_url_list)))
>>>>>>> 43567257373d9ac14581ca41683499833791eb71
		try:
			self.mycursor.execute(sql2,val2)
			self.sqldb.commit()
		except:
			print('fail!!!!')
			self.sqldb.rollback()
<<<<<<< HEAD


=======
# 		self.mycursor.execute(sql2,val2)
# 		self.sqldb.commit()
>>>>>>> 43567257373d9ac14581ca41683499833791eb71
	def begin(self):
		'''
			begin the use of API
		'''
		try:
			self.credential()
			self.preprocess()
			self.getInfo()
		except Exception:
			print('error! please enter the right number or ID')
			self.begin()
		else:
			self.implement()

def create_datebase():
	'''
		this part is for creating the mysql database
	'''
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="12345678"
	)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE twitter_mysql")

	mycursor.execute("SHOW DATABASES")
	for x in mycursor:
		print(x)

def create_table():
	'''
		this part is for creating the mysql table
	'''
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="12345678",
		database= 'twitter_mysql'
	)
	mycursor = mydb.cursor()
	sql1 = '''
		CREATE TABLE user(
		id int(5) primary key,
		username VARCHAR(255))
	'''
	mycursor.execute(sql1)
	sql2 = '''
		CREATE TABLE activity(
		username VARCHAR(255),
		searchID VARCHAR(255),
		searchNum VARCHAR(255),
		searchDate VARCHAR(255),
		imageNum VARCHAR(255))
		-- primary key(username,searchDate))
	'''
	mycursor.execute(sql2)

	mycursor.execute("SHOW TABLES")
	for x in mycursor:
		print(x)

def reset():
	'''
		this part is for reset the mysql database
	'''
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="12345678",
	)
	mycursor = mydb.cursor()
	mycursor.execute("drop database twitter_mysql")
	create_datebase()
	create_table()


restart = True
if restart:
	reset()


user_list = ['a','b','c','d','e']
for i in range(10):
	username = choice(user_list)
	user = twitter_API(username)
	user.mongodb()
	print('............successfully connect to mongodb..............')
	user.connect_mysql()
	print('............successfully connect to mysql..............')
	user.begin()
	user.insert()
	print('............finished insert mongodb...............')
	user.insert_mysql(i)
	print('............finished insert mysql...............')
	

	# print(user.client.list_database_names())
	# print(user.mydb.list_collection_names())
	# print(' ')
# user.video()
# print('............video finished..............')
exit(0)
