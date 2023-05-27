import cv2
import sys

class FaceDetection:
    process_current_frame= True

    def detect(self):
        video=cv2.VideoCapture(0)

        if not video.isOpened():
            sys.exit("Video not found")

        while True:
            ret, img = video.read()
            if self.process_current_frame:
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                haar_cascade = cv2.CascadeClassifier("cascade.xml")
                faces = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors=5)
            self.process_current_frame = not self.process_current_frame
            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow("Face",img)  
            if cv2.waitKey(1)==ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()


f_d = FaceDetection()
f_d.detect()

