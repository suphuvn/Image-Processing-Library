'''
Created on 2019 M11 5

@author: BrayamBoukhman
'''
from PIL import Image

def scaleImage(myImage, width, height):
    W, H=myImage.size
    
    FactorW=width/W
    FactorH=height/H
    
    scaledImage=Image.new("L", (width,height))
    
    for col in range(width):
        for row in range(height):
            p=myImage.getpixel((col/FactorW,row/FactorH))
            scaledImage.putpixel((col,row), p)
    return scaledImage