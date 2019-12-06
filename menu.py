'''
Created on 2019 M11 9

@author: BrayamBoukhman
'''
from PIL import Image
from filter import *
from crop import cropImage
from scaling import scaleImage
from blackandwhite import *
from featureVector import getFeatureVector
from database import *
from thinning import thining
from compareFilters import comparefilter
import copy
import featureVector
from multiChar import splitChar,conectCharScale



while True:
    #welcome user 
    print("{0:-^50s}".format(''))
    print("{0:*^50s}".format('  Main Menu  '))
    print("{0:-^50s}".format(''))
    print("{0:^50s}".format('CP467 Final Project.'))
    print("{0:^50s}".format('please select an option'))
    print()
    
    # gives the user the choice of what to do
    print("{0:^50s}".format('1. filter demonstration'))
    print("{0:^50s}".format('2. connected regions demonstration'))
    print("{0:^50s}".format('3. convolution comparison'))
    print("{0:^50s}".format('4. scaling demonstration'))
    print("{0:^50s}".format('5. thin demonstration'))
    print("{0:^50s}".format('6. store values in database'))
    print("{0:^50s}".format('7. Character Recognition'))
    print("{0:^50s}".format('8. Quit'))
    
    #gets the users responce
    print()
    optionPicked=input('Enter your choice here: ')
    print()
    #filter
    if optionPicked=="1":
        while True:
            print("{:-^25}".format("-"))
            print("{: ^25s}".format("Filtering"))
            print("{:-^25}".format("-"))

            print("     1. Blur")
            print("     2. Sharpen")
            print("     3. Edge Detection")
            print("     4. Custom")
            print("     5. Back")
            print()
            option1 = int(input("Enter choice: "))
            print()
            #get the kernel
            if option1==1:
                kernel=[1/18, 1/8, 1/18, 1/8, 1/4, 1/8, 1/18, 1/8, 1/16]
                break 
            elif option1==2:
                kernel=[0, -1, 0, -1, 5, -1, 0, -1, 0]
                break 
            elif option1==3:
                kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1]
                break
            elif option1==3:
                kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1]
                break
            elif option1==4:
                kernel = []
                print("Please enter the 9 kernel values from top left to bottom right")
                print("Please only enter in integers and decimals example(1,2,3,0.5,0.6) etc.")
                for m in range(1, 10):
                    kernelinput = float(input("Please enter the {0}th value: ".format(m)))
                    kernel.append(kernelinput)
                break
            else:
                print("invalid option, please try again")
        while True:
            filename = input('Please enter the filename for the image you wish to filter: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        imgFiltered=applyFilter(imgBase, kernel)
        imgBase.show()
        imgFiltered.show()
    #gotta wait for Erwin
    elif optionPicked=="2":
        while True:
            filename = input('Please enter the filename for the image you wish count pixels in connected regions: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        imgs=splitChar(imgBase)
        print(countMultiB(imgs))
        imgBase.show()
    #gotta show the comparisong between 
    elif optionPicked=="3":
        while True:
            filename = input('Please enter the filename for the image: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        comparefilter(imgBase)
    #scaling example
    elif optionPicked=="4":
        print("note that new width and height of image cannot be a decimal")
        newWidth=int(input("please enter new desired width"))
        newHeight=int(input("please enter new desired height"))
        while True:
            filename = input('Please enter the filename for the image: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        scaledImages=splitChar(imgBase)
        scaledImages=conectCharScale(scaledImages,newWidth,newHeight)
        imgBase.show()
        scaledImages.show()
    #thining demonstrations
    elif optionPicked=="5":
        while True:
            filename = input('Please enter the filename for the image: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
                
        imgBase.show()
        thinImage=thining(imgBase)
        thinImage.show()
    elif optionPicked=="6":
        while True:
            filename = input('Please enter the filename for the image: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        
        database=input("please enter the number in the image you wish to store")
        addValuesToDB(imgBase,database)
    elif optionPicked=="7":
        while True:
            filename = input('Please enter the filename for the image being recognized: ')
            try:
                imgBase = Image.open(filename).convert("L")
                print('')
                print('Image imported successfully')
                print('')
                break
            except IOError:
                print("Image import failed - file not found")
        temp=findCharacter(imgBase)
        print("the number in the image is ", temp)
        answer=input("was the recogniton correct (Y/N)")
        if answer=='N':
            database=input("please enter the number of the image")
            addValuesToDB(imgBase,database)
            
    #user exists the program 
    elif optionPicked=="8":
        print("quitting program.")
        break
    else:
        print()
        print("invalid menu option, please try again")
        print()
    
    
    
    