'''
Created on 2019 M11 9

@author: BrayamBoukhman
'''
from PIL import Image
from euclideanDistance import *
from featureVector import getFeatureVector
from crop import cropImage
from scaling import *
from thinning import *
from blackandwhite import convertBW


#fill in the database 
def addValuesToDB(img,database):
    fileLocation="DB/DB"+str(database)+".txt"
    print(fileLocation)
    f=open(fileLocation, "a")
    #apply thining croping and scaling then get feature vector and store it
    imgStore=scaleImage(cropImage(thining(img)), 100, 100)
    temp=str(getFeatureVector(imgStore))+'\n'
    f.write(temp)
    f.close()

#returns 2d array of feature of vectures in order of 0_9
def selectFromDB(database):
    fileLocation="DB/DB"+str(database)+".txt"
    f=open(fileLocation, "r")
    valuesDB=[]
    line=f.readline()
    while line:
        temp=line.replace('[', '')
        temp=temp.replace(']', '')
        temp=temp.replace(',','')
        temp=temp.split()
        [float(i) for i in temp]
        valuesDB.append(temp)
        line=f.readline()
    f.close()
    return valuesDB
#given 2d array of made from select From DB and feature vector
#of number trying to be found
def findCharacter(img):
    imgTest=scaleImage(cropImage(thining(img)), 100, 100)
    testVector=getFeatureVector(imgTest)
    predictN=0
    minValue=999999999
    for i in range(0,10):
        temp=averageDB(i)
        print(euclideanDistance (testVector, temp))
        if euclideanDistance (testVector, temp)<minValue:
            minValue=euclideanDistance (testVector, temp)
            predictN=i
    return predictN
def averageDB(database):
    valuesDB=selectFromDB(database)
    valuesAV=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    for i in valuesDB:
        for x in range(0,9):
            valuesAV[x]+=float(i[x])
    for x in range(0,9):
        valuesAV[x]=valuesAV[x]/len(valuesDB)
    return valuesAV