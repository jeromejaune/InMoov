from time import sleep
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
# start a opencv service
 
opencv = Runtime.start("opencv","OpenCV")
python = Runtime.start("python","Python")
gui = Runtime.start("gui","SwingGui")
arduino = Runtime.createAndStart("arduino","Arduino")
servoHB = Runtime.start("servoHB","Servo")
servoGD = Runtime.start("servoGD","Servo")
bouche= Runtime.start("bouche","Servo")
 
# add python as a listener to OpenCV data
# this tells the framework - whenever opencv.publishOpenCVData is invoked
# python.onOpenCVData will get called
python.subscribe("opencv", "publishOpenCVData")

arduino.connect("COM4")
servoHB.setMinMax(0, 180)
servoGD.setMinMax(0, 180)
bouche.setMinMax(0, 90)
   
# attach servo
servoHB.attach(arduino.getName(), 5)
servoGD.attach(arduino.getName(), 3)

print ("debut")
global posHB
global posGD
posGD = 100
posHB = 130
servoGD.moveTo(posGD)
sleep(1)
servoHB.moveTo(posHB)
sleep(1)
 
# call back - all data from opencv will come back to 
# this method
def onOpenCVData(data):
  # check for a bounding box
  if data.getBoundingBoxArray() != None:
    for box in data.getBoundingBoxArray():
     X = int(box.x * 100)
     Y = int(box.y * 100)
     if(X < 40):
      global posGD
      posGD -= 3
      servoGD.moveTo(posGD)
     elif(X > 60):
      global posGD
      posGD += 3
      servoGD.moveTo(posGD)
     if(Y < 40):
      global posHB
      posHB -= 3
      servoHB.moveTo(posHB)
     elif(Y > 60):
      global posHB
      posHB += 3
      servoHB.moveTo(posHB)

#newY = int(box.y * 100) + 50
#newX = int(box.x * 100) + 50
#servoHB.moveTo(newY)
#servoGD.moveTo(newX)
# to capture from an image on the file system
# opencv.captureFromImageFile("C:\Users\grperry\Desktop\mars.jpg")
gui.undockTab("opencv")

opencv.capture()

opencv.addFilter("FaceDetect")
opencv.setDisplayFilter("FaceDetect")
