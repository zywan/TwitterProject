#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:55:23 2018

@author: wzy
"""

import tweepy
from tweepy import OAuthHandler
import twitter_credential
import download_image
import numpy


auth = OAuthHandler(twitter_credential.consumer_key, twitter_credential.consumer_secret)
auth.set_access_token(twitter_credential.access_token, twitter_credential.access_token_secret)
api = tweepy.API(auth)

## get information of user
inf = api.get_user('wanzhangyu1')

# print (inf)
# home tweets
public_tweets = api.home_timeline()
#for tweet in public_tweets:
     #print(tweet.text)
## get tweet

## number of tweets
tweetNum = 100    
tweets = api.user_timeline(id = 'NBA', count = tweetNum)
#print(len(tweets))
#outfuck = open("out.txt","w")
#print(tweets[1],file=outfuck)
#outfuck.close()
#for ktweet in tweets:
    #print (ktweet.text)


## get the path of image
image_url_list = []
for status in tweets:
    #print(str(status.text)+'\n')
    
    for media in status.entities.get('media',[]):
        
        #print(media)
        image_url_list.append(media.get("media_url"))
        
# print(image_url_list)
#for image_url in image_url_list:
download_image.download_image(image_url_list)
#   