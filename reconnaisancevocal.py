
webgui = Runtime.start("webgui","WebGui")
webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
 
def onText(data):
     print data
     if (data == "sorry"):
     	print ("ca marche")
 
webkitspeechrecognition.addListener("publishText","python","onText")