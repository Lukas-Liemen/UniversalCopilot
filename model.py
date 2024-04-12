import json
import requests
from pyautogui import typewrite


class ChatModel:
    def __init__(self, api_key):
        self.url = ""  # Enter the URL of the chat model here
        self.api_key = api_key

        self.headers = {
            "X-API-KEY": self.api_key
        }

    def call(self, message):
        data = {"content": message}

        # Send the message
        wait = True
        with requests.get(self.url, headers=self.headers, json=json.dumps(data), stream=True) as r:
            for chunk in r.iter_content(1024):
                decoded = chunk.decode("utf-8")
                if wait:
                    if "\n" in decoded:
                        wait = False
                else:
                    typewrite(decoded)


model = ChatModel("")

def model_call(text):
    global model
    model.call(text)