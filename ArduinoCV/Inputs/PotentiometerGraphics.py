from cvzone.SerialModule import SerialObject
import cv2 
import numpy as np 

arduino = SerialObject("COM6")
while True:
    data = arduino.getData()
    print(data[0])
    img = cv2.imread("Resources/Potentiometer.jpg")
    try:                         # to resolve some unwanted errors we use try except method
        dialVal = data[0]
        cv2.putText(img , dialVal.zfill(4) , (260,280) , cv2.FONT_HERSHEY_PLAIN , 3 ,(255,255,255) , 3)
        if dialVal != '0':       # here the 0 value in data[] is a string so '' is used in if condition 
            dialVal = np.interp(int(dialVal),[0,1023],[-90,270])
            cv2.ellipse(img , (320,265) , (131,131) , 0 , -90 , dialVal , (255,180,0) , 10)

    except:
        pass

    cv2.imshow("image",img)
    cv2.waitKey(1)

