# start the services
from time import sleep
python = Runtime.start("python","Python")
clock = Runtime.start("clock2","Clock")
log   = Runtime.start("log","Log")


# define a ticktock method
def ticktock(timedata):
    print str(timedata)[11:3]
    
 
#create a message routes
clock.addListener("pulse", python.name, "ticktock")
clock.addListener("pulse","log","log")
 
# start the clock
clock.setInterval(1000)
clock.startClock()
# optional : wait the first loop before execution start
# clock.startClock(1