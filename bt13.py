import cv2 
from PIL import Image 
import numpy as np 

filehinh = r'lena.jpg'

img = cv2.imread(filehinh,cv2.IMREAD_COLOR)


imgPIL = Image .open(filehinh)

# vide ham tinh vecto trung binh mau
def TINHVECTOA(imgPIL):
    R1=0
    G1=0
    B1=0
    for x in range (80, 150, 1): 
        for y in range (400, 500, 1): 

            R,G,B = imgPIL.getpixel((x,y))
            R1+=R
            G1+=G
            B1+=B
    # kich thudc
    size = abs(80-150)*abs(400-500)
    R1 /= size
    G1 /= size
    B1 /= size
    return R1,G1,B1
R1,G1,B1 = TINHVECTOA(imgPIL)
def KIEMTRAPHANDOAN(imgPIL,R1,G1,B1):

    HINHPHANOOAN = Image.new(imgPIL.mode, imgPIL.size)
    
    width = imgPIL.size[0]
    height = imgPIL.size[1]
    
    D0 = 45
    
    for x in range (width): 
        for y in range(height):
            
            R, G, B = imgPIL.getpixel((x,y))

            
            D = np.sqrt(pow((R-R1),2)+pow((G-G1),2)+pow((B-B1),2))
            if(D < D0):
                Rd = 255
                Gd = 255
                Bd = 255
            else:
                Rd = R
                Gd = G
                Bd = B
            HINHPHANOOAN.putpixel((x,y),(Bd,Gd,Rd))
    return HINHPHANOOAN

a =  KIEMTRAPHANDOAN(imgPIL,R1,G1,B1)
hinhphandoan = np.array(a)
#cho hiển thị 
cv2.imshow("Anh goc", img)
cv2.imshow("Anh sau khi phan doan" ,hinhphandoan)

#bấm bất kỳ phím nào để đóng 
cv2.waitKey(0)


cv2.destroyAllWindows()
          



 

