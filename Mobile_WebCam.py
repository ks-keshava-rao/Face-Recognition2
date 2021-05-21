# Use your android mobile phone camera as your webcam
# Install IP webcam from Play store into your smartphone.
# connect your phone and pc with same wifi network
import urllib.request
import cv2
import numpy as np
import imutils
# Enter the url you got on the IP webcam application
url = 'http://192.168.137.139:8080/shot.jpg'
while True:
    imgPath = urllib.request.urlopen(url)
    imgNP = np.array(bytearray(imgPath.read()), dtype=np.unit8)
    img = cv2.imdecode(imgNP, -1)
    img = imutils.resize(img, width=450)
    cv2.imshow("CameraFeed", img)
    if ord('q') == cv2.waitKey(1):
        exit(0)