'''
Created on 2019 M11 7

@author: BrayamBoukhman
'''
from PIL import Image

def thining(img):
    imgTemp=Image.new("1", (img.width-1, img.height-1))
    pixelCounter=0
    deleted=False
    run=True
    size=(img.width-1)*(img.height-1)
    imgA=[]
    countDeleted=0
    
    while run:
        
        for i in range(0, img.width-1):
            for j in range(0, img.height-1):
                del imgA[:]
                imgA=getPixels(i,j,img)
                deleted, imgTemp=checkRules(i, j, imgA, imgTemp, img, deleted)
                pixelCounter+=1
                if deleted:
                    countDeleted+=1
            if pixelCounter==size:
                if deleted==True:
                    deleted=False
                    i=0
                    j=0
                    pixelCounter=0
                    countDeleted=0
                    img.paste(imgTemp,(0,0,imgTemp.width,imgTemp.height))
                else:
                    run=False
    return imgTemp
                
def getPixels(i,j,img):
    imgA=[]
    if (i == 0 or j == 0):                            
        imgA.append(255)
    else:               
        imgA.append(img.getpixel((i-1, j-1)))      
                    
    if j == 0:                                     
        imgA.append(255)
    else:
        imgA.append(img.getpixel((i, j-1)))           
    if j == 0:                                      
        imgA.append(255)    
    else:
        imgA.append(img.getpixel((i+1, j-1)))       
                
    if  i == 0:                                   
        imgA.append(255)
    else:   
        imgA.append(img.getpixel((i-1, j)))       
                    
    imgA.append(img.getpixel((i, j)))              
    imgA.append(img.getpixel((i+1, j)))           
                
    if i == 0:                                      
        imgA.append(255)
    else:
        imgA.append(img.getpixel((i-1, j+1)))      
                    
    imgA.append(img.getpixel((i, j+1)))             
    imgA.append(img.getpixel((i+1, j+1))) 
    return imgA 

def checkRules(i,j,imgA,imgTemp,img,deleted):
    #rule 1
    if (imgA[0]==0 and imgA[3]==0 and imgA[4]==0 and imgA[6]==0 and imgA[7]==0 and imgA[2]==255 and imgA[5]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                     
    #rule 2
    elif (imgA[0]==0 and imgA[1]==0 and imgA[3]==0 and imgA[4]==0 and imgA[6]==0 and imgA[5]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)  
        deleted = True              
    #rule 3 
    elif (imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[4]==0 and imgA[5]==0 and imgA[6]==255 and imgA[7]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True              
                    
    #rule 4
    elif (imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[3]==0 and imgA[4]==0 and imgA[7]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True              
    #rule 5
    elif (imgA[0]==0 and imgA[3]==0 and imgA[4]==0 and imgA[2]==255 and imgA[5]==255 and imgA[7]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                     
    #rule 6 
    elif (imgA[0]==0 and imgA[1]==0 and imgA[4]==0 and imgA[5]==255 and imgA[6]==255 and imgA[7]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True               
    #rule 7
    elif (imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[3]==0 and imgA[4]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0 and imgA[5]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                 
    #rule 8
    elif (imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[3]==0 and imgA[4]==0 and imgA[5]==0 and imgA[6]==0 and imgA[8]==0 and imgA[7]==255):
        imgTemp.putpixel((i,j),255) 
        deleted = True   
    #rule 9
    elif (imgA[3]==0 and imgA[4]==0 and imgA[6]==0 and imgA[1]==255 and imgA[2]==255 and imgA[5]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True
    #rule 10
    elif (imgA[4]==0 and imgA[6]==0 and imgA[7]==0 and imgA[0]==255 and imgA[1]==255 and imgA[2]==255 and imgA[5]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True              
    #rule 11
    elif (imgA[1]==0 and imgA[2]==0 and imgA[4]==0 and imgA[3]==255 and imgA[6]==255 and imgA[7]==255 and imgA[8]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True              
    #rule 12
    elif (imgA[2]==0 and imgA[4]==0 and imgA[5]==0 and imgA[0]==255 and imgA[3]==255 and imgA[6]==255 and imgA[7]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                                   
    #rule 13 
    elif (imgA[4]==0 and imgA[7]==0 and imgA[8]==0 and imgA[0]==255 and imgA[1]==255 and imgA[2]==255 and imgA[3]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True             
    #rule 14
    elif (imgA[4]==0 and imgA[5]==0 and imgA[8]==0 and imgA[0]==255 and imgA[1]==255 and imgA[3]==255 and imgA[6]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                
    #rule 15
    elif (imgA[0]==0 and imgA[1]==0 and imgA[2]==0 and imgA[4]==0 and imgA[5]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0 and imgA[3]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True   
    #rule 16 
    elif (imgA[0]==0 and imgA[2]==0 and imgA[3]==0 and imgA[4]==0 and imgA[5]==0and imgA[6]==0 and imgA[7]==0 and imgA[8]==0 and imgA[1]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True             
    #rule 17
    elif (imgA[2]==0 and imgA[4]==0 and imgA[5]==0 and imgA[7]==0 and imgA[8]==0 and imgA[0]==255 and imgA[3]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                 
    #rule 18
    elif (imgA[1]==0 and imgA[2]==0 and imgA[4]==0 and imgA[5]==0 and imgA[8]==0 and imgA[3]==255 and imgA[6]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                
    #rule 19
    elif (imgA[4]==0 and imgA[5]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0 and imgA[0]==255 and imgA[1]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True              
    #rule 20
    elif (imgA[3]==0 and imgA[4]==0 and imgA[6]==0 and imgA[7]==0 and imgA[8]==0 and imgA[1]==255 and imgA[2]==255):
        imgTemp.putpixel((i,j),255)
        deleted = True                                    
    else:
        imgTemp.putpixel((i,j),img.getpixel((i,j)))
    return deleted,imgTemp