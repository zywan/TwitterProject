# TwitterProject
# operation instruction
##  1. Get the tweets by using Tweepy
### 1.1 Get the credential
Finish the twitter.credential.py by inputting your personal credential and save it.
### 1.2 Crawling the tweets of some users
### 1.3 Find the URL of media and make them into a string[]
## 2. Download the Images
Run the mainFunction.py
Attention!!!     
in line 29, you can change the number of tweets you want to crawling.     
in line 31, you can change the ID of twitter account which you want to crawling.     
in download_image.py, you can change the path that you save the images depends on your preferance.   

## 3. Use Google vision to analysis the image and combine the labels and images
### 3.1 First, typing following code in terminal to get the permission
Attention! you have to change the path to your path of your PC/Mac    
export GOOGLE_APPLICATION_CREDENTIALS="input your path of the key json file"   
### 3.2 Run the label.py to get the labels of the images
## 4.convert images to a video
Run the convert_video.py    
Be attention to change to your personal path where you save the images
