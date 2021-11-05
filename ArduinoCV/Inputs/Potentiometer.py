from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM6")

while True:
    data = arduino.getData()
    print(data[0])

