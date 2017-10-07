from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
 
from time import sleep
 
servoPin = 3
# comPort = "/dev/ttyUSB0"
comPort = "COM5"
 
# create the services
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
 
# initialize arduino
# arduino.connect("/dev/ttyUSB0")
arduino.connect(comPort)
 
# TODO - set limits
servo01.setMinMax(0, 180)
   
# attach servo
servo01.attach(arduino.getName(), servoPin)
 
# fast sweep

# speed changes  
servo01.setSpeed(0.97) # set speed to 99% of full speed
servo01.moveTo(40) 
sleep(5)
 
servo01.setSpeed(0.97) # set speed to 50% of full speed
servo01.moveTo(110)
sleep(5)
 
servo01.setSpeed(1.0) # set speed to 100% of full speed
 
# moving to rest position
servo01.rest()
sleep(1)
 
# detaching servo
servo01.detach()