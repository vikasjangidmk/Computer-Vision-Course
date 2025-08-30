import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 255, 0, 0  # Blue-Green-Red 0,0,0

## Create a line
# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  # BGR (img, start, end, color, thickness)

## Rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 0), 3)
# cv2.rectangle(img, (0, 0), (250, 350), (0, 255, 0), cv2.FILLED)  # cv2.FILLED or -1 to fill the rectangle

# ## Create a circle
# cv2.circle(img, (400, 50), 50, (255, 255, 0), 5)  # (img, center, radius, color, thickness)

## Put Texts
cv2.putText(img, "Vikas Jangid", (200,440), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1)  # (img, text, org, font, fontScale, color, thickness)


cv2.imshow("Image", img)
cv2.waitKey(0)