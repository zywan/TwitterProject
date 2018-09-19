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
#inf = api.get_user('wanzhangyu1')

## home tweets
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
     #print(tweet.text)

## number of tweets
tweetNum = 100
## ID of tweet account
tweetID = 'NBA'    
tweets = api.user_timeline(id = tweetID, count = tweetNum)

## get the path of image
image_url_list = []
for status in tweets:
    
    for media in status.entities.get('media',[]):
        
        image_url_list.append(media.get("media_url"))

## download images
download_image.download_image(image_url_list)
