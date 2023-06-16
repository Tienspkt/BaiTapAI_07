import cv2 # xit dung thu vién xir
from PIL import Image # Thy vién xir ly anh P:
import numpy as np # thu vién ton ha11oc py
# lay dudng dln file hinh I

filehinh = r'lena.jpg'
#doc anh mau ding thy vign Opencv
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
hinhgoc = Image.open(filehinh)

# viet ham chuyén 664 dnh xém
def CHUYENDOIANHMUCXAM (hinhgoc) :

    average = Image.new(hinhgoc.mode, hinhgoc. size)
    # Ly kich thude anh
    width = hinhgoc. size[0]
    height= hinhgoc.size[1]
    for x in range (width):
        for y in range (height):
            # lay gia tri kênh x,y
            R, G, B = hinhgoc.getpixel((x,y))
            gray = np.uint8((R+G+B)/3)
            average. putpixel((x,y), (gray, gray, gray))
    return average 
avarage = CHUYENDOIANHMUCXAM(hinhgoc)
hinhmucxam = np.array(avarage)
#/ viết hàm nhận dạng đường biên 
def NHANDANGDUONGBIEN(average):
    # tg0 anh cé cing kich thude va mode so véi anh xém
    HINHLAYBIEN = Image.new(average.mode, average.size)
    # Ly kich thude anh
    width = average.size[0]
    height = average. size[1]
    # ma trgn theo phuong x
    matnalocx = np.array([(-1,-2,-1),(0,0,0),(1,2,1)],dtype=int)
     # ma trgn theo phuong y
    matnalocy = np.array([(-1,0,1),(-2,0,2),(-1,0,1)],dtype=int)
    Rnx=0
    Rny=0
    M0 =0
    xt= 0
    yt=0
    # quét tat ca céc diém anh
    for x in range (1,width-1):
        for y in range (1,height-1):
            Rnx=0
            Rny=0
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
                    R,G,B= avarage.getpixel((xt,yt))
                    # cong don
                    Rnx += (R*matnalocx[i,j])
                    Rny += (R*matnalocy[i,j])
                    M0 = np.abs(Rnx) + np.abs(Rny)
            # xét điều kiện 
            if M0 > 130:
                M0 = 255
            else:
                M0 = 0
            HINHLAYBIEN.putpixel((x,y),(M0,M0,M0))        
    return HINHLAYBIEN

anhnhandangbien = NHANDANGDUONGBIEN(avarage)
hinhnhandangbien = np.array(anhnhandangbien)
#cho hiển thị 
cv2.imshow("anh goc", img)
cv2.imshow("hinh nhan dang bien  ",hinhnhandangbien)

#bấm bất kỳ phím nào để đóng 
cv2.waitKey(0)

#6181 phéng b} nhé d& cép phat
cv2.destroyAllWindows()
