# Library for common saying and general statements / functions


import datetime

########## Init ##########

assistant_name = "Jarvis"

status = [
	"feeling life",
	"high on life",
	"hanging",
	"good and well, well and good",
	"feeling energetic",
	"doing my thang"
]

okays = [
	"kk",
	"on it",
	"will do",
	"working on it",
	"hold on",
	"hold your horses",
	"can do",
	"okeydokay"
]

doings = [
	"calculating mass of the earth",
	"squats",
	"yoga",
	"nothing",
	"ordering pizza",
	"shots",
	"studying for finals week",
	"hanging there"
]

########## Fx ##########

def greeting():
	time = int(datetime.datetime.now().hour)
	if (time >= 0) and (time <= 12):
		return f"Good Morning, i am your assistant {assistant_name}, how can i be of service"
	elif (time >12):
		return f"Good Afternoon, i am your assistant {assistant_name}, how can i be of service"
	else:
		return f"Hello, i am your assistant {assistant_name}, how can i be of service"
