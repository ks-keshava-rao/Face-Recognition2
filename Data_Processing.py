import cv2
import os
path = 'Rawdata/yuzvendra_chahal' # Source Folder
dstpath = 'datasets/yuzvendra_chahal' # Destination Folder
haar_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
(width, height) = (130, 100)

try:
    mkdir(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

files = os.listdir(path)
count = 1
for image in files:
    img = cv2.imread(os.path.join(path, image))
    gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    cv2.imwrite(os.path.join(dstpath, image), gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        faceOnly = gray[y:y + h, x:x + w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite(os.path.join(dstpath, image), faceOnly)

