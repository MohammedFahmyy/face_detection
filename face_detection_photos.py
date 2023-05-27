import os
import cv2
import imutils

class FaceDetection:

    def detect(self):
        path = r"C:\Users\the5b\Desktop\Test"
        Files = os.listdir(path)
        for File in Files:
            imgpath = os.path.join(path,File)
            img = cv2.imread(imgpath)
            img = imutils.resize(img, width=800)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier("cascade.xml")
            faces = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=5)
            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.imshow("Face",img)
            cv2.waitKey(0)        
            if cv2.waitKey(1)==ord('q'):
                break


f_d = FaceDetection()
f_d.detect()

