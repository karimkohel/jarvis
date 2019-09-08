########## Imports ##########

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

########## Fx ##########

def say(text):
	tts = gTTS(text=text, lang='en')
	filename = 'voice.mp3'
	tts.save(filename)
	playsound.playsound(filename)

def get():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google
		except Exception as e:
			print(" exception is : " + str(e))
	return said



# just testin the function and any runtime errors on my machine
say("hello there")

# fully functional
get()