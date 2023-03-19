# import os
# import cv2
# import imutils
# import imshow as imshow
#
# # img = cv2.imread("F:/AI Master Class/ab.png")
# # grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#color conversion -color gray
# # thresImg=cv2.threshold(grayImg,180,255,cv2.THRESH_BINARY)[1]
# # cv2.imshow("abb.png",thresImg)
# # print(img.shape)
#
# # cv2.imshow('Image', img)
# vs = cv2.VideoCapture(1)
# while True:
#     _, img = vs.read()
#     cv2.imshow("VedioStream",img)
#     key =cv2.waitKey(1) & 0xFF
#     if key == ord("q"):
#         break
# vs.release()
# cv2.destroyAllWindows()


# default camera code
import cv2

# create a video capture object
cap = cv2.VideoCapture(0)

# check if the camera is opened successfully
if not cap.isOpened():
    print("Unable to connect to camera")
    exit()

# read frames from the camera
while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # check if the frame is valid
    if not ret:
        print("Error capturing frame")
        break

    # display the frame
    cv2.imshow("Video Stream", frame)

    # exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

