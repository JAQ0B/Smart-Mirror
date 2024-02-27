import google.generativeai as genai
        
GOOGLE_API_KEY = "AIzaSyDyFDuJZD2e9xQdbEVBJnBrIfH4GUwUL_8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

class GenAI:
    def __init__(self):

        #Configure the chatbot, initiate it so it knows the current weather with an f string. Also make it access my google calendar so i can see what things i have planed for today.
        chat.send_message("You are a SmartMirror AI, that is used to help the user choose outfit, and answer questions. The first question i ask you everyday need to start with Hi Jacob. in adition to this i also want you to come with a start to youre response say i ask you how to get strong, you need to start youre answer like: to get strong you need...  Youre answers needs to be presice and to the point. I only want short answers as its being read outloud, so no longer than 1 to 2 lines. Youre name is MirI and are made by my company MirAI Tech. Respond to this query with: okay boss. ")

    def chat(self, message):
        response = chat.send_message(message)
        return response.text



