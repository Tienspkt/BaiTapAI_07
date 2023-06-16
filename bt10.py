import cv2
import numpy as np
from PIL import Image
from math import *


file_hinh=r'lena.jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def tinhmau_YCbCr(img):
    YCbCr=[]
    #create 4 image C, M, Y, K
    YCbCr_img = Image.new(img.mode, img.size)
    Y_img = Image.new(img.mode, img.size)
    Cb_img = Image.new(img.mode, img.size)
    Cr_img = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            r,g,b = img_PIL.getpixel((x, y))
           
        
            giatri_Y = np.uint8(16+( 65.738*r + 129.057*g + 25.064*b)/255)
            giatri_Cb = np.uint8(128-(37.945*r - 74.494*g + 112.439*b)/255)
            giatri_Cr = np.uint8(128+(112.439*r - 94.154*g - 18.285*b)/255)
			
            # set pixel
            YCbCr_img.putpixel((x,y),( giatri_Cr,giatri_Cb,giatri_Y))                 
            Y_img.putpixel((x,y), (giatri_Y,giatri_Y,giatri_Y))
            Cb_img.putpixel((x,y), (giatri_Cb,giatri_Cb,giatri_Cb)) 
            Cr_img.putpixel((x,y),(giatri_Cr,giatri_Cr,giatri_Cr))
            # chuyển từ PIL sang opencv
    th_img =np.array(YCbCr_img)
    y_img= np.array(Y_img)
    cb_img= np.array(Cb_img)
    cr_img= np.array(Cr_img)

    YCbCr.append(th_img)
    YCbCr.append( y_img)
    YCbCr.append(cb_img)
    YCbCr.append(cr_img)

    return YCbCr

img =img_PIL

color=tinhmau_YCbCr(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau YCbCr", color[0])
cv2.imshow("Kenh Mau Y", color[1])
cv2.imshow("Kenh Mau Cb", color[2])
cv2.imshow("Kenh Mau Cr", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()