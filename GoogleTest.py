import io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()
def getLabel(file_name):
# The name of the image file to annotate

#file_name = '/Users/wang/Desktop/twitterProject/images/1.jpg'

# Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    label_sum = []
    for label in labels:
       label_sum.append(label.description)
    return label_sum
    #label_sum = ''
    #print('Labels:')
    #for label in labels:
     #   label_sum = label_sum + label.description + ','
    #print(label_sum)
    #return label_sum

#print(getLabel("/Users/wang/Desktop/twitterProject/images/1.jpg"))
#print(type(getLabel("/Users/wang/Desktop/twitterProject/images/1.jpg")))
    