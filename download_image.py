#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:52:11 2018

@author: wzy
"""

import random
import urllib.request

def download_image(url_list):
    #name = random.randrange(1,1000)
    #filename = '/Users/wang/Desktop/twitterProject/images/'+str(name)+ '.jpg'
    #urllib.request.urlretrieve(url,filename)
	x = 0
	for item in url_list:
		filename = '/Users/wang/Desktop/twitterProject/images/%s.jpg' % x
		urllib.request.urlretrieve(item,filename)
		x+=1
