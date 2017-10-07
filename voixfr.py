#start Service
mouth = Runtime.start("MarySpeech", "MarySpeech")

mouth.setVoice("upmc-pierre-hsmm")

mouth.speakBlocking("bonjour je suis la voix francaise")

