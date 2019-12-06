from PIL import Image
import math
from filter import applyFilter


def comparefilter(img):
    print("first we will apply a horizontal 3*1/3 filter")
    firstImage=applyFilter(img, [0,0,0,1/3,1/3,1/3,0,0,0])
    print("second we will apply a vertical 3*1/3 filter and show it")
    firstImage=applyFilter(firstImage, [0,1/3,0,0,1/3,0,0,1/3,0])
    firstImage.show()
    print("lastly i will apply a 3*3*1/9 filter to the original image and show it")
    secondImage=applyFilter(img, [1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9,1/9])
    secondImage.show()
    print("when comparing the images it is clear they are the same")
    print("meaning both the 1/3 filters is the same as the 1/9 fitler")