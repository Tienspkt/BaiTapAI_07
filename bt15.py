import cv2 
from PIL import Image 
import numpy as np 

filehinh = r'lena.jpg'
#doc anh mau ding thy vign Opencv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
hinhgoc = Image.open(filehinh)
def NHANDANGDUONGBIEN(average):
    HINHLAYBIEN = Image.new(average.mode, average.size)
    # Ly kich thude anh
    width = average.size[0]
    height = average. size[1]
    matnalocx = np.array([(-1,-2,-1),(0,0,0),(1,2,1)],dtype=int)
     # ma trgn theo phuong y
    matnalocy = np.array([(-1,0,1),(-2,0,2),(-1,0,1)],dtype=int)
    xt= 0
    yt=0
    # quét tat ca céc diém anh
    for x in range (1,width-1,1):
        for y in range (1,height-1,1):
            Rx=0
            Gx=0
            Bx=0
            
            Ry=0
            Gy=0
            By=0
            for i in range (0,3,1):
                for j in range (0,3,1):
                    if(i ==0):
                        xt= x-1
                    elif(i==1):
                        xt = x
                    elif(i==2):
                        xt= x+1

                    if(j == 0):
                        yt= y-1
                    elif(j==1):
                        yt=y
                    elif(j==2):
                        yt=y+1
                    R,G,B= hinhgoc.getpixel((xt,yt))
                    # cong don
                    Rx += (R*matnalocx[i,j])
                    Gx += (G*matnalocx[i,j])
                    Bx += (B*matnalocx[i,j])

                    Ry += (R*matnalocx[i,j])
                    Gy += (G*matnalocx[i,j])
                    By += (B*matnalocx[i,j])
                    # tinh gxx
                    gxx = np.abs(Rx)**2 + np.abs(Gx)**2 + np.abs(Bx)**2
                    # tinh gyy
                    gyy = np.abs(Ry)**2 + np.abs(Gy)**2 + np.abs(By)**2
                    #tinh gxy
                    gxy = (Rx*Ry)+(Gx*Gy)+(Bx*By)

                    # tính theta
                    theta = 0.5*np.arctan2((2*gxy),(gxx-gyy))

                    #tính M0
                    M0 = np.sqrt(((gxx-gyy)/2+(gxx-gyy)*np.cos(2*theta)+2*gxy*np.sin(2*theta)))
            # xét điều kiện 
            if M0 > 130: # ngưỡng là 130 
                M0 = 255
            else:
                M0 = 0
            HINHLAYBIEN.putpixel((x,y),(M0,M0,M0))        
    return HINHLAYBIEN
anhnhandangbien = NHANDANGDUONGBIEN(hinhgoc)
hinhnhandangbien = np.array(anhnhandangbien)
#cho hiển thị 
cv2.imshow("anh goc", img)
cv2.imshow("hinh nhan dang bien  ",hinhnhandangbien)

#bấm bất kỳ phím nào để đóng 
cv2.waitKey(0)

#6181 phéng b} nhé d& cép phat
cv2.destroyAllWindows()