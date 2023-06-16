import cv2 
from PIL import Image 
import numpy as np 


filehinh = r'lena.jpg'

img = cv2.imread(filehinh,cv2.IMREAD_COLOR)


imgPIL = Image .open(filehinh)


img_sharp = Image.new(imgPIL.mode, imgPIL. size)
# lấy kích thước ảnh 
Width = img_sharp.size[0]
Height = img_sharp.size[1]

# tao 1 ma tran 3x3
mark3x3 = [[0,-1,0],[-1,4,-1],[0,-1,0]]

# quét tat ca céc diém anh
for x in range (1,Width-1):
    for y in range (1,Height-1):
        # biến chứa giá trị công dồn 
        Rs = 0
        Gs = 0
        Bs = 0
    
        for a in range (x-1,x+2):
            for b in range (y-1,y+2):
                 
                Red,Green,Blue = imgPIL.getpixel((a,b))
                
                Rs +=  Red * mark3x3[abs(x-a-1)][abs(y-b-1)]

                Gs +=  Green * mark3x3[abs(x-a-1)][abs(y-b-1)]

                Bs +=  Blue * mark3x3[abs(x-a-1)][abs(y-b-1)]
        
        R,G,B = imgPIL.getpixel((x,y))
        
        sharpR = R + Rs
        sharpG = G + Gs
        sharpB = B + Bs
        #Xét điều kiện 
        
        if(sharpR<0):
            sharpR = 0
        elif(sharpR>255):
            sharpR = 255
        else:
            sharpR = sharpR


        if(sharpG < 0):
            sharpG = 0
        elif (sharpG > 255):
            sharpG = 255
        else:
            sharpG = sharpG


        if (sharpB < 0):
            sharpB = 0
        elif (sharpB > 255):
            sharpB = 255
        else:
            sharpB = sharpB

        # lấy ảnh làm nét 
        img_sharp.putpixel ((x,y),(sharpB, sharpG, sharpR))
        print(x,y)

anh_sharp = np.array(img_sharp)
#cho hiển thị 
cv2.imshow("Anh goc", img)
cv2.imshow("Anh sac net" ,anh_sharp)

#bấm bất kỳ phím nào để đóng 
cv2.waitKey(0)

#6181 phéng b} nhé d& cép phat
cv2.destroyAllWindows()



 



                    


 

