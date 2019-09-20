########## Imports ##########
import speech_recognition as sr
import pyttsx3
import sayings

########## Init ##########

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

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

########## Main ##########
if __name__ == '__main__':
	speak(sayings.greeting())
