# start a opencv service
 
opencv = Runtime.start("opencv","OpenCV")
python = Runtime.start("python","Python")
gui = Runtime.start("gui","SwingGui")
 
# add python as a listener to OpenCV data
# this tells the framework - whenever opencv.publishOpenCVData is invoked
# python.onOpenCVData will get called
python.subscribe("opencv", "publishOpenCVData")
 
 
# call back - all data from opencv will come back to 
# this method
def onOpenCVData(data):
  # check for a bounding box
  if data.getBoundingBoxArray() != None:
    for box in data.getBoundingBoxArray():
    int X = box.x *100
      print(X, box.y, box.width)
 
# to capture from an image on the file system
# opencv.captureFromImageFile("C:\Users\grperry\Desktop\mars.jpg")
gui.undockTab("opencv")

opencv.capture()

opencv.addFilter("FaceDetect")
opencv.setDisplayFilter("FaceDetect")
