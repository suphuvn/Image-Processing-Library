'''
Created on 2019 M11 11

@author: BrayamBoukhman
'''
from PIL import Image
from crop import cropImage
from scaling import scaleImage
import copy



def splitChar(myImage):
    # Array of images of characters in myImage to run through OCR algorithm
    characters = []
    # Array of pixels already found
    recorded = []

    for i in range(myImage.height):
        for j in range(myImage.width):
            # Pixel to test
            testPixel = myImage.getpixel((j,i))
            # If the pixel is non-white and has not already been found
            if testPixel != 255 and notRecorded(recorded, j, i):
                # A new character has been found in the image!
                # Create a blank new image to record the character (same height and width as the original)
                newImage = Image.new("L", (myImage.width, myImage.height), color=255)
                newImage, recorded = pixelSearch(myImage, newImage, recorded, [j, i])
                characters.append(copy.deepcopy(newImage))

    return characters

def pixelSearch(originalImage, newImage, recorded, curPixel):
    if originalImage.getpixel((curPixel[0], curPixel[1])) != 255 and notRecorded(recorded, curPixel[0], curPixel[1]):
        # Add the current pixel in the same location to the new image
        newImage.putpixel((curPixel[0], curPixel[1]), originalImage.getpixel((curPixel[0], curPixel[1])))
        # Add the current pixel to the recorded array
        recorded.append(copy.deepcopy(curPixel))
        #here is where recurtion is done
        #case 1 where it is the top left pixel
        if not(curPixel[0]==0 or curPixel[1]==0):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] - 1,curPixel[1] - 1])
        #case 2 where it is top pixel
        if not(curPixel[1]==0):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0],curPixel[1] - 1])
        #case 3 where it is top right
        if not(curPixel[0]==originalImage.width-1 or curPixel[1]==0):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] + 1,curPixel[1] - 1])
        #case 4 where it is left pixel
        if not(curPixel[0]==0):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] - 1,curPixel[1]])
        #case 5 where it is right pixel
        if not(curPixel[0]==originalImage.width-1):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] + 1,curPixel[1]])
        #case 6 where it is bottom left
        if not(curPixel[0]==0 or curPixel[1]==originalImage.height-1):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] - 1,curPixel[1] + 1])
        #case 7 where it is bottom
        if not(curPixel[1]==originalImage.height-1):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0],curPixel[1] + 1])
        #case 8 where it is bottom right
        if not(curPixel[0]==originalImage.width-1 or curPixel[1]==originalImage.height-1):
            newImage, recorded = pixelSearch(originalImage, newImage, recorded, [curPixel[0] + 1,curPixel[1] + 1])
    return newImage, recorded
        
        
def notRecorded(recorded, x, y):
    result = True
    for item in recorded:
        if item[0] == x and item[1] == y:
            result = False

    return result

def conectCharScale(imgs,width,height):
    cols=imgs[0].height
    rows=imgs[0].width
    newImage = Image.new("L", (rows, cols), color=255)
    for img in imgs:
        pixelLoc=find_firstPixel(img)
        temp=cropImage(img)
        temp=scaleImage(temp,width,height)
        newImage.paste(temp, (pixelLoc[0],pixelLoc[1]))
    return newImage
def find_firstPixel(img):
    cols=img.height
    rows=img.width
    first=[0,0]
    for i in range(cols):
        for j in range(rows):
            if img.getpixel((j,i))!=255:
                first=[j,i]
                break
        if (first!=[0,0]):
            break
    return first