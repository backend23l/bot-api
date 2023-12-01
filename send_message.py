import requests
from settings import URL, chat_id


def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    requests.get(url, params=payload)

send_message(URL, chat_id, 'hi')
