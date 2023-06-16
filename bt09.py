import cv2
import numpy as np
from PIL import Image
from math import *


file_hinh=r'lena.jpg'
original_img = cv2.imread(file_hinh)
img_PIL = Image.open(file_hinh)

def Tinhmau_XYZ(img):
    XYZ=[]
    #create 4 image C, M, Y, K
    XYZ_img = Image.new(img.mode, img.size)
    X_img = Image.new(img.mode, img.size)
    Y_img = Image.new(img.mode, img.size)
    Z_img = Image.new(img.mode, img.size)

    # get size of original_img
    height = img.size[0]
    width = img.size[1]
    for x in range(height):
        for y in range(width):
            # get pixel at point (x,y)
            r,g,b = img_PIL.getpixel((x, y))
        
            giatri_X = np.uint8(0.4124564*r + 0.3575761*g + 0.1804375*b)
            giatri_Y = np.uint8(0.2126729*r + 0.7151522*g + 0.0721750*b)
            giatri_Z = np.uint8(0.0193339*r + 0.1191920*g + 0.9503041*b)
			
            # set pixel
            XYZ_img.putpixel((x,y), (giatri_Z,giatri_Y,giatri_X))        
            X_img.putpixel((x,y), (giatri_X,giatri_X,giatri_X))          
            Y_img.putpixel((x,y), (giatri_Y,giatri_Y,giatri_Y))
            Z_img.putpixel((x,y),(giatri_Z,giatri_Z,giatri_Z))
            # chuyển từ PIL sang opencv
    xyz_img =np.array(XYZ_img)
    x_img= np.array(X_img)
    y_img= np.array(Y_img)
    z_img= np.array(Z_img)

    XYZ.append(xyz_img)
    XYZ.append(x_img)
    XYZ.append(y_img)
    XYZ.append(z_img)

    return XYZ

img =img_PIL

color=Tinhmau_XYZ(img)
           #convert image to array (show image by opencv)

# show image
cv2.imshow("HINH GOC", original_img)
cv2.imshow("Kenh Mau XYZ", color[0])
cv2.imshow("Kenh Mau X", color[1])
cv2.imshow("Kenh Mau Y", color[2])
cv2.imshow("Kenh Mau Z", color[3])

cv2.waitKey(0)
cv2.destroyAllWindows()