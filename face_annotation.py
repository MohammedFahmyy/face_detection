import os
import cv2

class FaceAnnotation:

    def detect(self):
        f = open("pos.txt",'w')
        path = "pos"
        Files = os.listdir(path)
        for File in Files:
            imgpath = os.path.join(path,File)
            img = cv2.imread(imgpath)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            faces = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=5)
            if(len(faces)==0):
                os.remove(imgpath)
            for x,y,w,h in faces:
                if(len(faces)==1):
                    Dir = imgpath + " " + str(1)
                    Dir = Dir + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                    print(Dir)
                    f.write(Dir+"\n")
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                else:
                    os.remove(imgpath)
                    break
            cv2.imshow("Face",img)
            cv2.waitKey(1000)        
            if cv2.waitKey(1)==ord('q'):
                break
        f.close()


f_d = FaceAnnotation()
f_d.detect()

