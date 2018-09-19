import cv2
import matplotlib.pyplot as plt
import GoogleGetLabel
import os
from PIL import Image, ImageDraw, ImageFont

filePath = '/Users/wang/Desktop/twitterProject/images/'
for file in os.listdir(filePath):
	if file.endswith(".jpg"):
		filename = filePath + file
		
## Get labels:
		try:
			labels = GoogleTest.getLabel(filename)
		except Exception:
			print("Error, please give the right filename")
		# use the default (fond) tff
		font=cv2.FONT_HERSHEY_SIMPLEX 
 	
		im = cv2.imread(filename)

		i = 50
		for label in labels:
			# # 2 means font size，（50,i）is initial place，(69,0,255) is color of font，2 is font weight
			im=cv2.putText(im,label,(50,i),font,2,(69,0,255),3)
			i = i+60

		cv2.imwrite(filename,im)
		
