from langchain_ollama import ChatOllama


class OllamaService:
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, messages):
        llm = ChatOllama(model=self.model_name,temperature=0,)
        response = llm.invoke(messages)
        return response
