'''
Created on 2019 M09 30

@author: BrayamBoukhman
'''
from PIL import Image
from pip._vendor.pyparsing import downcaseTokens


#Converts image from grayscale to black and White

def convertBW(img):
    for i in range(img.width):
        for j in range(img.height):
            if img.getpixel((i,j))>140:
                img.putpixel((i,j),255)
            else:
                img.putpixel((i,j),0)
    return img

def invert(img):
    cols=img.width
    rows=img.height
    a = [[0 for i in range(cols)] for j in range(rows)] 
    for i in range(img.width):
        for j in range(img.height):
            if img.getpixel((i,j)) == 255:
                a[j][i]=-1
                img.putpixel((i,j), 0)
            else:
                img.putpixel((i,j), 255)

    return img


def countB(img): #[y][x]
    cols=img.height
    rows=img.width
    count=0
    for i in range(cols):
        for j in range(rows):
            if img.getpixel((j,i))!=255:
                count+=1
    return count

def countMultiB(imgs):
    numberOfPixels=[]
    for i in imgs:
        i.show()
        print(countB(i))
        numberOfPixels.append(countB(i))
    return numberOfPixels



