#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:52:11 2018

@author: wzy
"""

import random
import urllib.request

def download_image(url_list):
	x = 0
	for item in url_list:
		# /Users/wang/Desktop/twitterProject/images/ <-- this part depends on which path to save the image
		filename = '/Users/wang/Desktop/twitterProject/images/%s.jpg' % x
		urllib.request.urlretrieve(item,filename)
		x+=1
