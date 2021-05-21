import cv2
import os
haar_file = 'haarcascade_frontalface_default.xml'
#create
datasets = 'datasets'
sub_data = 'keshav'

path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)
cam = cv2.VideoCapture(0)
count = 1
while count < 51:
    print(count)
    (_, im) = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)
        faceOnly = gray[y:y+h, x:x+w]
        resizeImg = cv2.resize(faceOnly, (width, height))
        cv2.imwrite("%s/%s.jpg" % (path,  count), faceOnly)
        count = count + 1
    cv2.imshow("FaceDetection", im)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("image captured successfull")
cam.release()



