import os
from services.ollama_service import OllamaService
from langchain_core.chat_history import InMemoryChatMessageHistory
from services.google_genai_service import GoogleGenaiService
from utils.constants import SYSTEM_PROMPT, MODEL_NAME

# The use of this service is to persist messages in a chat session.
# But, it currently the tool doesn't work like a chatbot.
# TODO: Implement the chat functionality.
class MessagePersistenceService:
    def __init__(self):
        self.chats_by_session_id = {}

    def call_model(self, state, config):
        if "configurable" not in config or "session_id" not in config["configurable"]:
            raise ValueError(
                "Make sure that the config includes the following information: {'configurable': {'session_id': 'some_value'}}"
            )
        # Fetch the history of messages and append to it any new messages.
        chat_history = self.get_chat_history(config["configurable"]["session_id"])
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + list(chat_history.messages) + state["messages"]
        if os.getenv("USE_OLLAMA") == "true":
            # If the environment variable USE_OLLAMA is set to true,
            # we will use the Ollama service to call the model.
            ai_message = OllamaService(MODEL_NAME).ask(messages)
        else:
            ai_message = GoogleGenaiService(MODEL_NAME).ask(messages)
        # Finally, update the chat message history to include
        # the new input message from the user together with the
        # response from the model.
        chat_history.add_messages(state["messages"] + [ai_message])
        return {"messages": ai_message}

    def get_chat_history(self, session_id):
        chat_history = self.chats_by_session_id.get(session_id)
        if chat_history is None:
            chat_history = InMemoryChatMessageHistory()
            self.chats_by_session_id[session_id] = chat_history
        return chat_history
