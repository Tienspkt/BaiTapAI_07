
import cv2              # Sử dụng thư viện xử lý ảnh openCV
from PIL import Image   # Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np      # Sử dụng thư viện toán học, đặc biệt là các tính toán ma trận 
import math

# Khai báo đường dẫn file hình
picture = r'bird_small.jpg'

# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(picture, cv2.IMREAD_COLOR)

imgPIL = Image.open(picture)

Smoothed_3x3_picture = Image.new(imgPIL.mode, imgPIL.size)   # Copy các chế độ(mode) và kích thước của ảnh
Smoothed_5x5_picture = Image.new(imgPIL.mode, imgPIL.size)
Smoothed_7x7_picture = Image.new(imgPIL.mode, imgPIL.size)
Smoothed_9x9_picture = Image.new(imgPIL.mode, imgPIL.size)

# Lấy kích thước của ảnh từ imgPIL
width = Smoothed_3x3_picture.size[0]         # chiều ngang
height = Smoothed_3x3_picture.size[1]        #chiều cao

# Mỗi ảnh là 1 ma trận 2 chiều nên sử dụng 2 vòng for để quét hết tất cả các điểm ảnh(pixel) có trong ảnh đang xét
def Smoothed_3x3_img() :
    for x in range(1, width-1):
        for y in range(1, height-1):
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    # Lấy giá trị điểm ảnh tại vị trí (x, y)
                    R, G, B = imgPIL.getpixel((i, j))   
                    Rs += R
                    Gs += G
                    Bs += B                      
            K = 3*3
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)
            Smoothed_3x3_picture.putpixel((x, y), (Bs, Gs, Rs))  

def Smoothed_5x5_img() :
    for x in range(2, width-2):
        for y in range(2, height-2):
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x-2,x+3):
                for j in range(y-2,y+3):
                    # Lấy giá trị điểm ảnh tại vị trí (x, y)
                    R, G, B = imgPIL.getpixel((i, j))   
                    Rs += R
                    Gs += G
                    Bs += B                      
            K = 5*5
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)
            Smoothed_5x5_picture.putpixel((x, y), (Bs, Gs, Rs))  

def Smoothed_7x7_img() :
    for x in range(3, width-3):
        for y in range(3, height-3):
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x-3,x+4):
                for j in range(y-3,y+4):
                    # Lấy giá trị điểm ảnh tại vị trí (x, y)
                    R, G, B = imgPIL.getpixel((i, j))   
                    Rs += R
                    Gs += G
                    Bs += B                      
            K = 7*7
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)
            Smoothed_7x7_picture.putpixel((x, y), (Bs, Gs, Rs))  

def Smoothed_9x9_img() :
    for x in range(4, width-4):
        for y in range(4, height-4):
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x-4,x+5):
                for j in range(y-4,y+5):
                    # Lấy giá trị điểm ảnh tại vị trí (x, y)
                    R, G, B = imgPIL.getpixel((i, j))   
                    Rs += R
                    Gs += G
                    Bs += B                      
            K = 9*9
            Rs = np.uint8(Rs / K)
            Gs = np.uint8(Gs / K)
            Bs = np.uint8(Bs / K)
            Smoothed_9x9_picture.putpixel((x, y), (Bs, Gs, Rs))  

Smoothed_3x3_img()
Smoothed_5x5_img()
Smoothed_7x7_img()
Smoothed_9x9_img()

Smoothed_3x3_picture_display = np.array(Smoothed_3x3_picture) 
Smoothed_5x5_picture_display = np.array(Smoothed_5x5_picture)
Smoothed_7x7_picture_display = np.array(Smoothed_7x7_picture)
Smoothed_9x9_picture_display = np.array(Smoothed_9x9_picture)

# Resize ảnh cho vừa kích thước màn hình lap
resize = (417,318)
img_res = cv2.resize(img, resize, interpolation = cv2.INTER_AREA)
Smoothed_3x3_picture_display_res = cv2.resize(Smoothed_3x3_picture_display, resize, interpolation = cv2.INTER_AREA)
Smoothed_5x5_picture_display_res = cv2.resize(Smoothed_5x5_picture_display, resize, interpolation = cv2.INTER_AREA)
Smoothed_7x7_picture_display_res = cv2.resize(Smoothed_7x7_picture_display, resize, interpolation = cv2.INTER_AREA)
Smoothed_9x9_picture_display_res = cv2.resize(Smoothed_9x9_picture_display, resize, interpolation = cv2.INTER_AREA)

# Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau goc RGB co gai bird_small',img_res)
cv2.imshow('Hinh lam muot voi mat na 3x3', Smoothed_3x3_picture_display_res)
cv2.imshow('Hinh lam muot voi mat na 5x5', Smoothed_5x5_picture_display_res)
cv2.imshow('Hinh lam muot voi mat na 7x7', Smoothed_7x7_picture_display_res)
cv2.imshow('Hinh lam muot voi mat na 9x9', Smoothed_9x9_picture_display_res)

# Bấm phím bất kỳ để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

# Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()