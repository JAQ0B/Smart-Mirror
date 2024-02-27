from neuralintents.assistants import BasicAssistant

assistant = BasicAssistant("F:\Programming\Smart_Mirror\intents.json", model_name='SmartMirror')


assistant.fit_model(epochs=100)
print("Done Fitting")
assistant.save_model()

