import cv2
import numpy as np

## Resize image

# img = cv2.imread("resources/lambo.png")
# print(img.shape)
# resized_img = cv2.resize(img, (300,200))
# print(resized_img.shape)
# cv2.imshow("Output", img)
# cv2.imshow("Resized Output", resized_img)
# cv2.waitKey(0)


## Cropping image
img = cv2.imread("resources/lambo.png")
crop_img = img[0:200, 200:500]
cv2.imshow("Output", img)
cv2.imshow("Cropped Output", crop_img)
cv2.waitKey(0)
