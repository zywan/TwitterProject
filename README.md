# TwitterProject
# operation flow
##  1. Get the tweets by using Tweepy
### 1.1 Get the credential
### 1.2 Crawling the tweets of some users
### 1.3 Find the URL of media and make them into a string[]
## 2. Download the Images
run the mainFunction.py
## 3. Use Google vision to analysis the image and combine the labels and images
### 3.1 First, typing a sentence in terminal to get the permission
export GOOGLE_APPLICATION_CREDENTIALS="/Users/wang/Desktop/twitterProject/googleVisionPart/key.json" 
### 3.2 Run the label.py
## 4.convert images to a video
run the convert.py
