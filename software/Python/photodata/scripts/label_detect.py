from __future__ import print_function
from pymongo import MongoClient
from google.cloud import vision
import pymongo
import os
import io

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient.test

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shefalisharma/software/Python/photodata/scripts/photo-project-285122-a4a5d64aadaf.json"
client = vision.ImageAnnotatorClient()
directory = '/Users/shefalisharma/software/Python/photodata/input'


for filename in os.listdir(directory):
    image_uri = directory + '/' + filename
   
    imagetags = []
    with io.open(image_uri, 'rb') as image_file:
        content = image_file.read()
        image = vision.types.Image(content=content)
       
        response = client.label_detection(image=image)
        print('=' * 30)
        for label in response.label_annotations:
            imagetags.append(label.description)
            print(label.description, '(%.2f%%)' % (label.score*100.))

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        for landmark in landmarks:
            imagetags.append(landmark.description)
            print(landmark.description, '(%.2f%%)' % (landmark.score*100.))


        photodata = {
            'loc': image_uri,
            'tags': imagetags,
            'year': 2008,
            
        }
        mydb.photo.insert_one(photodata)
        