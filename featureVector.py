'''
Created on 2019 M11 5

@author: BrayamBoukhman
'''
from PIL import Image
import math

def percentOfPixels(img):
    count = 0 
    imgSize = img.width*img.height
    
    for i in range(img.width-1):
        for j in range(img.height-1):
            pixelValue = img.getpixel((i,j))
            if pixelValue == 0:
                count += 1
    
    percent = count/imgSize
    
    return round(percent, 4)

##         w33 w66 
##       --- --- --- 
##      | q1| q2| q3| 
##  h33  --- --- --- 
##      | q4| q5| q6| 
##  h66  --- --- --- 
##      | q7| q8| q9|
##       --- --- --- 
    
#divides the image into 9 regions all of equal size
#returns a feature vector

def getFeatureVector(img):
    
    i=0
    q=[]
    featureVectore=[]
    
    w33=math.ceil(img.width/3)      #1/3 of the image's width
    w66=math.ceil((img.width*2)/3) #2/3 of the image's width
    
    h33=math.ceil(img.height/3)      #1/3 of the image's width
    h66=math.ceil((img.height*2)/3) #2/3 of the image's width
    
    #First Row
    q.append(img.crop((0,0,w33,h33)))
    q.append(img.crop((w33,0,w66,h33)))
    q.append(img.crop((w66,0,img.width,h33)))
    #Second Row
    q.append(img.crop((0,h33,w33,h66)))
    q.append(img.crop((w33,h33,w66,h66)))
    q.append(img.crop((w66,h33,img.width,h66)))
    #Third Row
    q.append(img.crop((0,h66,w33,img.height)))
    q.append(img.crop((w33,h66,w66,img.height)))
    q.append(img.crop((w66,h66,img.width,img.height)))
    
    for i in q:
        featureVectore.append(percentOfPixels(i))
    return featureVectore
    
