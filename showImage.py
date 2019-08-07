import cv2
from PIL import Image
import numpy as np
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
#im = Image.open('data/Final Printpdf.442.jpg')
im=cv2.VideoCapture('Khiladi-786-movie-image.jpg')
check,img=im.read()
#img = np.array(im); # im2arr.shape: height x width x channel
img1 = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray,1.16, 5);
for (x,y,w,h) in faces:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('frame',img1);
if cv2.waitKey(10) & cv2.waitKey(0) == ord('q') :
    
    
    cv2.destroyAllWindows()
