import cv2
import urllib.request
import numpy as np

url='http://192.168.100.39/cam-hi.jpg'
cv2.namedWindow("Berhasil", cv2.WINDOW_AUTOSIZE)
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

while True:
    imgresponse=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imgresponse.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)

    cv2.imshow("Berhasil",img)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break

cv2.destroyAllWindows
