import sys
import threading
import tkinter as tk
import speech_recognition as sr
from Genai import GenAI

from neuralintents import BasicAssistant

from elevenlabs import generate, play, set_api_key
set_api_key("4b0dfa6d6503f2de4be1ab9839e2aea8")

GenAI = GenAI()

if response == "GenAI response":
    GenAI.chat(text)

elif response == "Clothing":
    
elif response == "Music":
    
elif response == "Weather":
    
elif response == "Home":
    

wake_word = "hey jake"

class Assistant:


    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.speak("Starting...")

        self.assistant = BasicAssistant("F:\Programming\Smart_Mirror\intents.json")
        self.assistant.load_model('SmartMirror.keras')

        self.root = tk.Tk()
        self.label = tk.Label(text="O", font=("Arial", 120, "bold"))
        self.label.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_program)
        self.exit_button.pack()

        threading.Thread(target=self.run_assistant).start()

        self.root.mainloop()



    def exit_program(self):
        self.speak("Goodbye!")
        self.root.destroy()
        sys.exit(0)


    def speak(self, text):
        self.say = generate(
  	    text= text,
	    voice="Sarah",
  	    model="eleven_multilingual_v2"
	    )
        play(self.say) 
    
    def MoreHelp(self):
        with sr.Microphone() as mic:
            self.speak("Do you need any further help?")
            audio = self.recognizer.listen(mic, timeout=5, phrase_time_limit=3)
            text = self.recognizer.recognize_google(audio, language='en-in').lower()
            if "no" in text:
                return False
            else:
                return True

    def TakeCommand(self):
        with sr.Microphone() as mic:
            print("Wake word detected. Listening for command...")
            audio = self.recognizer.listen(mic, timeout=5, phrase_time_limit=10)
            text = self.recognizer.recognize_google(audio, language='en-in').lower()
            print("audio: ")
            print(audio)
            print("text: ")
            print(text)
            if text == "stop":
                self.speak("Bye")
                self.root.destroy()
                sys.exit()
            else:
                if text is not None:
                    response = self.assistant.process_input(text)
                    print("response: ")
                    print(response)
                    if response is not None:
                        self.speak(response)
                if text is "SwitchToSide2":
                    with open("config.js", "w") as f:
                        f.write("")        
                self.label.config(fg="black")

    def run_assistant(self):
         while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                    print("Listening for wake word...")
                    audio = self.recognizer.listen(mic, timeout=10, phrase_time_limit=3)
                    print(audio)

                    # Wake word detection using a dedicated library or a more advanced method
                    if wake_word in self.recognizer.recognize_google(audio, language='en-in').lower():
                        self.label.config(fg="red")
                        
                        self.TakeCommand()
                        while self.MoreHelp() == True:
                            self.TakeCommand()
                        self.label.config(fg="black")

            except:
                self.label.config(fg="black")
                continue


Assistant()
