import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print faceCascade.empty()
image = cv2.imread("photo.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceRecList = faceCascade.detectMultiScale(grayImage, 1.11, 3)

print "%d faces found" % len(faceRecList)

print "facelist = " , faceRecList

for (x,y,w,h) in faceRecList:
    #print '%d %d %d %d' % (x,y,w,h)
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2) # image, p1(bottom left), p2(top right), RGB, line-thickness
    
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()