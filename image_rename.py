#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:58:38 2018

@author: wzy
"""

import os

path_name='/Users/wang/Desktop/twitterProject/images/'

i=1
for item in os.listdir(path_name):
    os.rename(item,(str(i)+'.png'))
    i=i+1
        
j=1
for item in os.listdir(path_name):
    if item.endswith('.png'):
        os.rename(item,(str(j)+'.jpg'))
        j=j+1