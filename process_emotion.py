from __future__ import print_function
import time 
import requests
import cv2
import operator
import numpy as np


# Import library to display results
import matplotlib.pyplot as plt
##%matplotlib inline 
### Display images within Jupyter

# Variables

_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
_key = 'bc6345a975764d81bfc68674b28c5442' #Here you have to paste your primary key
_maxNumRetries = 10

def processRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
        
    return result

def face_rect(result):
    for currFace in result:
        faceRectangle = currFace['faceRectangle']
        cv2.rectangle( img,(faceRectangle['left'],faceRectangle['top']),
                           (faceRectangle['left']+faceRectangle['width'], faceRectangle['top'] + faceRectangle['height']),
                       color = (255,0,0), thickness = 5 )

    return faceRectangle

def face_emotion(result):

    emotion_1 = max(currFace['scores'].items(), key=operator.itemgetter(1))[0]
    emotion_2 = max(currFace['scores'].items(), key=operator.itemgetter(1))[1]
    emotion_3 = max(currFace['scores'].items(), key=operator.itemgetter(1))[2]
    
    return emotion_1, emotion_2, emotion_3


pathToFileInDisk = r'C:\Users\Administrator\Desktop\1.jpg'
with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'

json = None
params = None

result = processRequest( json, data, headers, params )

rect = face_rect(result)
emo1, emo2, emo3 = face_emotion(result)

print(rect)
print(emo1)
print(emo2)
print(emo3)
