import pyttsx3   #python librarary for text to speech
import datetime  #python library for date time

engine = pyttsx3.init('sapi5')   #microsift speech api
voices = engine.getProperty('voices')
engine.setProperty(voices,voices[0].id)  #setting male voice in system
def speak(audio):   #function  to speak
    engine.say(audio)
    engine.runAndWait()
def greet():    #function to greet when program first start
    time = int(datetime.datetime.now().hour)
    if(time > 0 and time<=12):
        speak("Good Morning")
    else:
        speak("Good evening")

if __name__ == '__main__':    #main
    greet()
    with open('textFile.txt','r') as read:  #opening file textFile
        lines = read.read()    #reading words in file
        speak(lines)    #calling speak function for speaking

