import cv2 #su dung thu vien opencv
import numpy as np #su dung thu vien toan hoc
from PIL import Image #thu vien su ly anh pillow ho tro dinh dang anh

#Khai bao duong dan file hinh
filehinh = r'lena.jpg'

#Doc anh goc RGB bang opencv
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
#Doc anh mau bang thu vien pillow
imgPIL = Image.open(filehinh)

#Lay kich thuoc anh
width = imgPIL.size[0]
height = imgPIL.size[1]



#Tao 4 anh chua ket qua chuyen doi cua cac kenh mau
cyan = Image.new(imgPIL.mode, imgPIL.size)
magenta = Image.new(imgPIL.mode, imgPIL.size)
yellow = Image.new(imgPIL.mode, imgPIL.size)
black = Image.new(imgPIL.mode, imgPIL.size)

#Quet tung diem anh bang 2 vong lap for
for x in range(width):
    for y in range(height):
        #Lay gia tri diem anh
        R, G, B = imgPIL.getpixel((x, y))
        #Set cac gia tri cua cac kenh mau bang cach tron mau voi nhau
        cyan.putpixel((x, y),(R, G, 0))
        magenta.putpixel((x,y),(R, 0, B))
        yellow.putpixel((x, y),(0, G, B))
        K = min(R, G, B )
        black.putpixel((x, y),(K, K , K))

#Chuyen anh PIL sang opencv
anhC = np.array(cyan)
anhM = np.array(magenta)
anhY = np.array(yellow)
anhK = np.array(black)

#Hien thi hinh cua opencv
cv2.imshow('Hinh goc RGB', img)
cv2.imshow('Hinh Lena kenh Cyan', anhC)
cv2.imshow('Hinh Lena kenh Magenta', anhM)
cv2.imshow('Hinh Lena kenh Yellow', anhY)
cv2.imshow('Hinh Lena kenh Black', anhK)

#Bam phim bat ky de dong cua so hien thi anh
cv2.waitKey(0)
#Giai phong bo nho cap cho
cv2.destroyAllWindows()