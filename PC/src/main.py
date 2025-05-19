import sys
import threading
import tkinter as tk
from tkinter import PhotoImage
import speech_recognition as sr
from Genai import GenAI

GenAI = GenAI()

from dotenv import load_dotenv
import os

load_dotenv()

from neuralintents import BasicAssistant

from elevenlabs import generate, play, set_api_key

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

from Raspberry.SendRequest import PageController

page_controller = PageController()

wake_word = "hey jake"


class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.speak("Starting...")

        self.assistant = BasicAssistant(
            "F:\Programming\Smart_Mirror\intents.json", model_name="SmartMirror"
        )
        self.assistant.load_model()

        self.root = tk.Tk()
        self.image1 = PhotoImage(file="chatbot1.png")
        self.image2 = PhotoImage(file="chatbot2.png")
        self.label = tk.Label(image=self.image1)
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
        self.say = generate(text=text, voice="Sarah", model="eleven_multilingual_v2")
        play(self.say)

    def MoreHelp(self):
        with sr.Microphone() as mic:
            self.speak("Do you need any further help?")
            audio = self.recognizer.listen(mic, timeout=5, phrase_time_limit=3)
            text = self.recognizer.recognize_google(audio, language="en-in").lower()
            if "no" in text:
                return False
            elif "yes" in text:
                return True

    def TakeCommand(self):
        with sr.Microphone() as mic:
            print("Wake word detected. Listening for command...")
            audio = self.recognizer.listen(mic, timeout=5, phrase_time_limit=10)
            text = self.recognizer.recognize_google(audio, language="en-in").lower()
            print("audio: ")
            print(audio)
            print("text: ")
            print(text)
            if text == "stop":
                self.exit_program()
            else:
                if text is not None:
                    response = self.assistant.process_input(text)
                    print("response: ")
                    print(response)

                    if response == "GenAI response":
                        self.speak(GenAI.chat(text))
                    elif response == "Clothing":
                        print("Switching to clothing")
                        page_controller.change_page(3)
                    elif response == "Music":
                        print("Switching to music")
                        page_controller.change_page(2)
                    elif response == "Weather":
                        print("Switching to weather")
                        page_controller.change_page(4)
                    elif response == "Home":
                        print("Switching to Home")
                        page_controller.change_page(1)

    def run_assistant(self):
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                    print("Listening for wake word...")
                    audio = self.recognizer.listen(mic, timeout=10, phrase_time_limit=3)
                    print(audio)

                    # Wake word detection using a dedicated library or a more advanced method
                    if (
                        wake_word
                        in self.recognizer.recognize_google(
                            audio, language="en-in"
                        ).lower()
                    ):
                        self.label.config(image=self.image2)

                        self.TakeCommand()
                        while self.MoreHelp() == True:
                            self.TakeCommand()
                        self.label.config(image=self.image1)

            except:
                self.label.config(image=self.image1)
                continue


Assistant()
