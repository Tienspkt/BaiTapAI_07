import cv2 as cv #   Thư viện OpenCV

img = cv.imread("lena.jpg", cv.IMREAD_COLOR)


red = img.copy()
green = img.copy()
blue = img.copy()

# R-G-B = (2,1,0)

red[:, :, 1] = 0
red[:, :, 0] = 0 

green[:, :, 2] = 0
green[:, :, 0] = 0


blue[:, :, 2] = 0
blue[:, :, 1] = 0


cv.imshow('Hinh mau RGB goc co gai Lena', img)
cv.imshow('Kenh RED', red)
cv.imshow('Kenh GREEN', green)
cv.imshow('Kenh BLUE', blue)


cv.waitKey(0)

cv.destroyAllWindows()

