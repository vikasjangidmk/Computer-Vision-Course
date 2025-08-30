import cv2

# img = cv2.imread("resources/lena.png")
# print(img)
# cv2.imshow("Output", img)
# cv2.waitKey(0)    


# # Reading Videos

# cap = cv2.VideoCapture("resources/elon.mp4")

# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow("Output", img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


## Reading from webcam

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100) # brightness

while True:
    success, img = cap.read()
    print(img.shape)
    cv2.imshow("Output", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break