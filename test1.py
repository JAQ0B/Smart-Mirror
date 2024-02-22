import time
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as mic:
    print("Default Energy Threshold:", recognizer.energy_threshold)

    # Collect energy threshold values for 5 seconds
    for _ in range(5):
        audio = recognizer.listen(mic)
        volume = recognizer.energy_threshold
        print("Volume Level:", volume)
        
        time.sleep(1)  # Wait for 1 second before the next measurement

    # Calculate the average energy threshold
    average_threshold = sum(recognizer.energy_threshold for _ in range(5)) / 5
    print("Average Energy Threshold:", average_threshold)
