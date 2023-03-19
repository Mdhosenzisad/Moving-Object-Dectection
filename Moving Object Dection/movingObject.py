import cv2
import time
import imutils ## image resize
# Create a VideoCapture object to capture frames from a video file
# create a video capture object
cap = cv2.VideoCapture(0)
time.sleep(1)
firstFrame=None
area = 500
# Create a background subtractor object
# fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the video
    # ret, frame = cap.read()
    _,img =cap.read()
    text = "Normal"
    img = imutils.resize(img,width=500)
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussianImg =cv2.GaussianBlur(grayImg, (21,21),0)
    if firstFrame is None:
        firstFrame = gaussianImg ##capturing 1st frame on iteration
        continue
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY) [1]
    threshImg = cv2.dilate(threshImg,None,iterations=2)
    cnts =cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area :
            continue
        (x, y, w, h) = cv2.boundingRect (c)
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)
        text="Moving Object Detection"
    print(text)
    cv2.putText(img,text,(10,20),
            cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    cv2.imshow("cameraFeed", img)
    key = cv2.waitKey(1) & 0xFF
    # Exit on key press
    if cv2.waitKey(1) == ord('q'):
            break




    #
    # # Apply background subtraction
    # # fgmask = fgbg.apply(frame)
    #
    # # Threshold the result
    # _, thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)
    #
    # # Perform morphological operations to remove noise
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #
    # # Find contours of moving objects
    # contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # Draw bounding boxes around the moving objects
    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #
    # # Display the result
    # cv2.imshow('Moving objects', frame)



  # Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
