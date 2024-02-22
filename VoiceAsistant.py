import speech_recognition as sr
from elevenlabs import generate, play, set_api_key


set_api_key("4b0dfa6d6503f2de4be1ab9839e2aea8")

def speak(text):
	audio = generate(
  	text= text,
	voice="Sarah",
  	model="eleven_multilingual_v2"
	)
	play(audio)
	

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query