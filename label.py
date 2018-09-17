import cv2
import matplotlib.pyplot as plt
import GoogleTest
import os
from PIL import Image, ImageDraw, ImageFont

filePath = '/Users/wang/Desktop/twitterProject/images/'
for file in os.listdir(filePath):
	if file.endswith(".jpg"):
		filename = filePath + file
		#print(filename)
		


# # Get labels:
		labels = GoogleTest.getLabel(filename)
		print(labels)
 #print(type(label))

		font=cv2.FONT_HERSHEY_SIMPLEX #使用默认字体
 	
		im = cv2.imread(filename)

		i = 50
		for label in labels:

			im=cv2.putText(im,label,(50,i),font,2,(69,0,255),3)
			i = i+60
# #添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细

		cv2.imwrite(filename,im)
		

		#base = Image.open(filename).convert('RGBA')

# make a blank image for the text, initialized to transparent text color
		#txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
		#fnt = ImageFont.truetype('/Users/wang/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSerif-BoldItalic.ttf', 10)
# get a drawing context
		#d = ImageDraw.Draw(txt)

# draw text, half opacity
		#d.text((20,20), label, font=fnt, fill=(255,48,48,128))
# draw text, full opacity
		
		#out = Image.alpha_composite(base, txt)
		#rgb_im = out.convert('RGB')
		#rgb_im.save(filename)
