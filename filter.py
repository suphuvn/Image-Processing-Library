from PIL import Image
import math


def applyFilter(img, kernel):
    i=0
    j=0
    filtered=Image.new("L", (img.width,img.height))
    
    for i in range(0, img.width-1):
        for j in range(0,img.height-1):
            #clear runtotal each loop
            runtotal=0
            #populate imageArray with top left pixel
            if not(i==0 or j==0):
                runtotal=runtotal+(kernel[0]*img.getpixel((i-1, j-1)))    
            #populate imageArray with top middle pixel
            if not(j==0):
                runtotal=runtotal+(kernel[1]*img.getpixel((i, j-1))) 
            #populate imageArray with top right pixel
            if not(i==img.width or j==0):
                runtotal=runtotal+(kernel[2]*img.getpixel((i+1, j-1))) 
            #populate imageArray with middle left pixel
            if not(i==0):
                runtotal=runtotal+(kernel[3]*img.getpixel((i-1, j)))
            #populate imageArray with middle pixel
            runtotal=runtotal+(kernel[4]*img.getpixel((i, j)))
            #populate imageArray with middle right pixel
            if not(i==img.width):
                runtotal=runtotal+(kernel[5]*img.getpixel((i+1, j)))
            #populate imageArray with bottom left pixel
            if not(i==0 or j==img.height):
                runtotal=runtotal+(kernel[6]*img.getpixel((i-1, j+1)))
            #populate imageArray with bottom middle pixel
            if not(j==img.height):
                runtotal=runtotal+(kernel[7]*img.getpixel((i, j+1)))
            #populate imageArray with bottom right pixel
            if not(i==img.width or j==img.height):
                runtotal=runtotal+(kernel[8]*img.getpixel((i+1, j+1)))
            filtered.putpixel((i,j), math.floor(runtotal))
    return filtered
