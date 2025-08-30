import cv2
import numpy as np

## Conver to Gray Scale

# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print("Color_img shape: ", img.shape)
# print("Gray_img shape: ", img_gray.shape)
# cv2.imshow("Color_img", img)
# cv2.imshow("Gray_img", img_gray)
# cv2.waitKey(0)

## Convert to blur image

# img = cv2.imread("resources/lena.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# print("Color_img shape: ", img.shape)
# print("Gray_img shape: ", img_gray.shape)
# print("Blur_img shape: ", img_blur.shape)
# cv2.imshow("Color_img", img)
# cv2.imshow("Gray_img", img_gray)
# cv2.imshow("Blur_img", img_blur)
# cv2.waitKey(0)

## Convert to cannyImg

img = cv2.imread("resources/lena.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img_blur, 100, 100)
print("Color_img shape: ", img.shape)
print("Gray_img shape: ", img_gray.shape)
print("Blur_img shape: ", img_blur.shape)
print("Canny_img shape: ", img_canny.shape)
cv2.imshow("Color_img", img)
cv2.imshow("Gray_img", img_gray)
cv2.imshow("Blur_img", img_blur)
cv2.imshow("Canny_img", img_canny)
cv2.waitKey(0)
