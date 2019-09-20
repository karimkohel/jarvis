########## Imports ##########

import os
import time
import playsound
import speech_recognition as sr
import pyttsx3
from gtts import gTTS

########## Init ##########

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

assistant_name = "Jarvis"

########## Fx ##########


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening ...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		query = r.recognize_google(audio,language='en-in')
		print("user :",query,"\n")
	except sr.UnkownValueError:
		speak("sorry didn't get that, try typing")
		query = str(input(" : "))
		print("\n")
	return query

def greet():
	time = int(datetime.datetime.now().hour)
	if (time >= 0) and (time <= 12):
		speak("Good Morning, i am your assistant",assistant_name)
		speak("how can i be of service")
	elif (time >12):
		speak("Good Afternoon, i am your assistant",assistant_name)
		speak("how can i be of service")
	else:
		speak("Hello, i am your assistant",assistant_name)
		speak("how can i be of service")

########## Main ##########
