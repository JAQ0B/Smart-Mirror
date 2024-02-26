from neuralintents.assistants import BasicAssistant

assistant = BasicAssistant("F:\Programming\Smart_Mirror\intents.json", model_name='SmartMirror')


assistant.fit_model(epochs=100)
assistant.save_model()

