import requests
from settings import chat_id,url
from time import sleep
while True:
    def send_massage(url:str,chat_id:int,text:str):
        endpoint = '/sendMessage'
        url+=endpoint
        payload = {
            'chat_id': 5815225140, #-1002102062683, #5128222065
            'text': text,
        }
        requests.get(url, params=payload)

    send_massage(url, chat_id, "Assalomu aleykum")
    sleep(0.3)
