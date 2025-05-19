Smart Mirror – Teknologi A Eksamen Projekt
This was our final group project (4 members) in "Teknologi A". We built a smart mirror that combines AI-based voice control, outfit suggestions, and a modular mirror interface powered by MagicMirror².

🔧 What works:
A Tkinter UI assistant running on PC:

Lights up when listening for voice commands.

Uses Google Gemini API to answer questions.

Understands commands like "show music" using intent recognition (trained model + intents.json).

Sends commands to the MagicMirror using a local API.

A random clothing suggestion module that shows outfit images using a local image dataset.

A basic Flask API for remote control via mobile phone.

The mirror shows the suggested outfit via image update.

⚠️ What’s missing:
AI was originally meant to run directly on the Raspberry Pi, but due to compute limitations and exam time pressure, this wasn’t completed.

Clothing suggestions are random, not based on weather or patterns yet.

Not fully integrated into one seamless Raspberry-based product (but the separate modules function individually).

🖥️ Technologies:
Python (Flask, Tkinter, neuralintents)

ElevenLabs (TTS)

Google Gemini (LLM)

MagicMirror² (Node.js, Raspberry Pi)

Basic ML model for intent classification

📦 Setup
Install Python requirements:

bash
Copy
Edit
pip install -r requirements.txt
Start the project:

bash
Copy
Edit
bash run.sh
See MagicMirror/config.js for installed modules and config.

🔗 MagicMirror Setup
We used MagicMirror² running on a Raspberry Pi with the following modules installed:

MMM-Weather

MMM-Remote-Control

MMM-Spotify (planned)

Custom CSS + image display module

📁 View config.js here

