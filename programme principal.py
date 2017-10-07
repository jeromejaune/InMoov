#start Service
from time import sleep
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime


opencv = Runtime.start("opencv","OpenCV")
wikidatafetcher = Runtime.start("wikidatafetcher","WikiDataFetcher")
python = Runtime.start("python","Python")
clock = Runtime.start("clock","Clock")
log   = Runtime.start("log","Log")
arduino = Runtime.createAndStart("arduino","Arduino")
servoHB = Runtime.start("servoHB","Servo")
servoGD = Runtime.start("servoGD","Servo")
bouche= Runtime.start("bouche","Servo")
audiofile = Runtime.createAndStart("audiofile", "AudioFile")
mouth = Runtime.start("MarySpeech", "MarySpeech")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
alice = Runtime.createAndStart("alice", "ProgramAB")
wikidatafetcher.setWebSite("frwiki")
wikidatafetcher.setLanguage("fr")
OpenWeatherMap=Runtime.createAndStart("OpenWeatherMap", "OpenWeatherMap")
OpenWeatherMap.setApiKey("votre key") #https://home.openweathermap.org/
OpenWeatherMap.setUnits("metric") # or imperial
OpenWeatherMap.setLang("fr") # en / de ...
mouth.setVoice("upmc-pierre-hsmm")
alice.startSession()
python.subscribe("opencv", "publishOpenCVData")


webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
webgui.startBrowser("http://localhost:8888/#/service/webkitspeechrecognition")

arduino.connect("COM4")
servoHB.setMinMax(0, 180)
servoGD.setMinMax(0, 180)
bouche.setMinMax(0, 90)

# attach servo
servoHB.attach(arduino.getName(), 5)
servoGD.attach(arduino.getName(), 3)
bouche.attach(arduino.getName(), 10)

global posHB
global posGD
posGD = 100
posHB = 130

servoGD.moveTo(100)
sleep(1)
servoHB.moveTo(130)
sleep(1)
bouche.moveTo(80)
mouth.speakBlocking("bonjour")
bouche.moveTo(0)
sleep(0.5)
print ("start")
date = 0
tempo = 0

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

def mouvbouche(etat):
	print ("bouche")

def ticktock(timedata):
    global date
    global tempo
    tempo = tempo + 1
    date = str(timedata)
    print tempo
    print date
    if (tempo == 5):
    		print ("ca fait 5")
    		reponse = str(alice.getResponse("alea"))[18:]
    		print ("Robot : " + reponse)
    		mouth.speakBlocking(reponse)
    		global tempo
    		tempo = 0

def Enleve_Accents(txt):
    ch1 = u"??????????????"
    ch2 = u"aaceeeeiiouuuy"
    s = ""
    for c in txt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s


def onText(datarec):
	data = Enleve_Accents(datarec)
	print ("humain : " + data)
	global tempo
	tempo = 0
	print tempo
	if ("r2 d2" in data):
		print ("Son R2D2")
		audiofile.playFile("C:\mrl\myrobotlab.1.0.2340\son\VeryExcitedR2D2.mp3")
		sleep(2)
		mouth.speakBlocking("desole j'avais un r2d2 coinc? dans la gorge")
	elif ("heure" in data):
		print date
		bouche.moveTo(80)
		mouth.speakBlocking("il est " + str(date)[11:-16] + " heures " + str(date)[14:-13])
		bouche.moveTo(00)
	elif ("meteo" in data):
		r=[]
		r=OpenWeatherMap.fetchRaw("ANGERS")
		print r[1]
		mouth.speakBlocking("il fait actuellement")
		mouth.speakBlocking(str(r[1]))
		mouth.speakBlocking("degr?s")
	elif ("tete" in data and "droite" in data):
		mouth.speak("ok")
     	#servoGD.setVelocity() # set velocity to something fast
		servoGD.moveTo(150)
	elif ("tete" in data and "gauche" in data):
		mouth.speak("ok")
     	#servoGD.setVelocity() # set velocity to something fast
		servoGD.moveTo(40)
	elif ("tete" in data and "basse" in data):
		mouth.speak("ok")
     	#servoGD.setVelocity() # set velocity to something fast
		servoHB.moveTo(160)
	elif ("tete" in data and "haute" in data):
		mouth.speak("ok")
     	#servoGD.setVelocity() # set velocity to something fast
		servoHB.moveTo(50)
	elif ("repos" in data):
		mouth.speak("ok")
     	#servoGD.setVelocity() # set velocity to something fast
   		servoGD.moveTo(100)
		sleep(1)
		servoHB.moveTo(130)
		sleep(1)
	elif ("Trouve moi la definition" in data):
		print u"c est quoi un ?l?phant  : " + wikidatafetcher.getDescription(u"?l?phant")
	else:
		reponse = str(alice.getResponse(data))[18:]
     	print ("Robot : " + reponse)
     	mouth.speak(reponse)
     	mouvbouche(1)
     	sleep(0.5)
     	mouvbouche(0)

clock.setInterval(60000)
clock.startClock()

webkitspeechrecognition.addListener("publishText","python","onText")
clock.addListener("pulse", python.name, "ticktock")
clock.addListener("pulse","log","log")
gui.undockTab("opencv")

opencv.capture()

opencv.addFilter("FaceDetect")
opencv.setDisplayFilter("FaceDetect")


