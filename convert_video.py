
import os
os.chdir('/Users/wang/Desktop/twitterProject/images/')
os.popen('ffmpeg -loop 1 -i %d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 0.5 -t 60 vedio_name.mp4','r',1)