# create a ProgramAB service and start a session
alice = Runtime.createAndStart("alice", "ProgramAB")
alice.startSession()


 url = alice.getResponse("How are you?")
 data = url.split("null") 
 print data[1]

