'''
Created on 2019 M09 11

@author: BrayamBoukhman
'''
from PIL import Image
from filter import applyFilter
from blackandwhite import convertBW,countB,invert
from compareFilters import comparefilter
from crop import cropImage
from scaling import scaleImage
from featureVector import getFeatureVector
from thinning import thining
from euclideanDistance import euclideanDistance
from database import addValuesToDB,selectFromDB, averageDB, findCharacter
from multiChar import splitChar,conectCharScale
from _ast import Invert


filename = "testing/numbers2.png"

try:
    imgBase = Image.open(filename).convert("L")
    print('')
    print('Image imported successfully')
    print('')
except IOError:
    print("Image import failed - file not found")


temp=splitChar(imgBase)
temp=conectCharScale(temp,30,30)
#for img in temp:
    #img.show()
imgBase.show()
temp.show()

#print(temp)
#print(imgStore.size)
#imgStore.show()

#filteredImage=applyFilter(imgBase,[-1, -1, -1, -1, 8, -1, -1, -1, -1])
#imgBase.show()
#filteredImage.show()






