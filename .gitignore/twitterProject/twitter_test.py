#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:55:23 2018

@author: wzy
"""

import tweepy
from tweepy import OAuthHandler
import twitter_credential
#import wget


auth = OAuthHandler(twitter_credential.consumer_key, twitter_credential.consumer_secret)
auth.set_access_token(twitter_credential.access_token, twitter_credential.access_token_secret)
api = tweepy.API(auth)

## get tweets

tweets = api.user_timeline(id = 'Kobe Bryant',cout = 1,)
print (tweets,"\n")

## get the path of image
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
        
## show the image
for media_file in media_files:
    print(media_file)

## download the image
#for media_file in media_files:
#    wget.download(media_file)
   