#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:52:11 2018

@author: wzy
"""

import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+ '.jpg'
    urllib.request.urlretrieve(url,full_name)

