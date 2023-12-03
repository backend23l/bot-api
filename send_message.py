import requests
from settings import url, chat_id


def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': 6268298385,
        'text': text,
    }
    requests.get(url, params=payload)

send_message(url, chat_id, 'Salom')
