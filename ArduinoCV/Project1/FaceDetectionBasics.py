import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.8)  # minimum face detection confidence is minimum percent required for successful face detection
while True:
    success, img = cap.read()
    img , bboxs = detector.findFaces(img) 
    cv2.imshow("FaceDetection Basics",img)
    cv2.waitKey(1) 