import cv2 as cv #thêm thưu viện
from PIL import Image # Thư viện PILLOW
import numpy as np #thư viện toán

#Khai báo đường dẫn
filehinh = r'lena.jpg'
# đọc bằng opencv
img = cv.imread(filehinh, cv.IMREAD_COLOR)

#đọc bằng PIL
imgPIL= Image.open(filehinh)

#sao chép hình ảnh
Tb_Average= Image.new( imgPIL.mode, imgPIL.size)
Tb_Lightness= Image.new( imgPIL.mode, imgPIL.size)
Tb_Luminance= Image.new( imgPIL.mode, imgPIL.size)
# lấy kích thước ảnh từ imPIl
width = Tb_Average.size[0]
height = Tb_Average.size[1]

# xử dụng vòng for để quét ảnh 
for x in range(width):
    for y in range (height):
        #lấy giá trị màu tại các cặp (x,y)
        R, G, B = imgPIL.getpixel((x,y))
        # chuển ảnh sang xám phương pháp tb
        gray_Average = np.uint8((R+G+B)/3)
         # giá giá trị về cho ảnh 
        Tb_Average.putpixel((x,y), (gray_Average, gray_Average, gray_Average))


        # chuyển ảnh sang xám phương pháp Lightness
        Max = max( R , G ,B)
        Min = min( R , G ,B)
        gray_Lightness = np.uint8((Max+Min)/2)
        Tb_Lightness.putpixel((x,y), (gray_Lightness, gray_Lightness, gray_Lightness))

        # chuyen ảnh sang xám phương pháp Luminance
        gray_Luminance = np.uint8(0.2126*R + 0.7152*G +0.0722*B)
        Tb_Luminance.putpixel((x,y), (gray_Luminance, gray_Luminance, gray_Luminance))


#chuyển đổi từ PIL về Opencv để hiển thị
anhmucxam_average = np.array(Tb_Average)
anhmucxam_lightness = np.array(Tb_Lightness)
anhmucxam_Luminance = np.array(Tb_Luminance)
# hiển thị 
cv.imshow ('Hinh co gai lena RGB ', img)
cv.imshow('Anh muc xam  Average', anhmucxam_average)
cv.imshow('Anh muc xam  Lightness', anhmucxam_lightness)
cv.imshow('Anh muc xam  Luminance', anhmucxam_Luminance)
#bấm phím bất kỳ
cv.waitKey(0)
#giải phóng bộ nhớ 

cv.destroyAllWindows