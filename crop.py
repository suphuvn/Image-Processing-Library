import sys
from PIL import Image
from itertools import count

def check(minOrMax, count, start):

    if minOrMax == "min":
        return count < start
    else:
        return count > start



#Runs through the image but only cares about the black pixels
#once it runs hits a white pixel, then itchecks if that new extreme
#is greater then or less then depending on the extreme being looked for
#------------------------------------------------------------------------
def findExtremeMaxX(myImage):
    xSize = myImage.size[0]
    ySize = myImage.size[1]
    
    outside = xSize
    inside = ySize
    
    start=0
    end=outside-1
    
    myValue=start
    for row in range(inside):
        count=end
        test = myImage.getpixel((count, row))
        
        while test == 255 and check("max", count, start):
            count-=1
            test=myImage.getpixel((count,row))
        if count>myValue:
            myValue=count
    
    return myValue


#---------------------------------------------------------------------
def findExtremeMaxY(myImage):
    xSize = myImage.size[0]
    ySize = myImage.size[1]
    
    outside = ySize
    inside = xSize
    
    start=0
    end=outside-1
    
    
    myValue=start
    for row in range(inside):
        count=end
        test = myImage.getpixel((row, count))
        
        while test == 255 and check("max", count, start):
            count-=1
            test=myImage.getpixel((row,count))
        if count>myValue:
            myValue=count
    return myValue


#------------------------------------------------------------------
def findExtremeMinX(myImage):
    xSize = myImage.size[0]
    ySize = myImage.size[1]
    
    outside = xSize
    inside = ySize
    
    start=outside-1
    end=0
    
    myValue=start
    for row in range(inside):
        count=end
        test = myImage.getpixel((count, row))
        
        while test == 255 and check("min", count, start):
            count+=1
            test=myImage.getpixel((count,row))
        if count<myValue:
            myValue=count
    return myValue

#---------------------------------------------------------------------
def findExtremeMinY(myImage):
    xSize = myImage.size[0]
    ySize = myImage.size[1]
    
    outside = ySize
    inside = xSize
    
    start=outside-1
    end=0
    
    outside = ySize
    inside = xSize
    
    
    myValue=start
    for row in range(inside):
        count=end
        test = myImage.getpixel((row, count))
        
        while test == 255 and check("min", count, start):
            count+=1
            test=myImage.getpixel((row,count))
        if count<myValue:
            myValue=count
    return myValue
def cropImage(myImage):

    xMin = findExtremeMinX(myImage)
    xMax = findExtremeMaxX(myImage)
    yMin = findExtremeMinY(myImage)
    yMax = findExtremeMaxY(myImage)

    myImage = myImage.crop((xMin, yMin, xMax+1, yMax+1))

    # Returns the scaled image
    return myImage