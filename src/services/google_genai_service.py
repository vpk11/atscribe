from langchain.chat_models import init_chat_model


class GoogleGenaiService:
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, messages):
        model = init_chat_model(self.model_name, model_provider="google_genai")
        response = model.invoke(messages)
        return response
