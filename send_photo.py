import requests
from settings import URL, chat_id


def send_photo(url: str, chat_id: int, photo: str):
    endpoint = '/sendPhoto'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'photo': photo
    }

    r = requests.post(url, params=payload)


photo = 'AgACAgIAAxkBAAPDZW2z5dLoKbj5nFXu8sojMg1CeQIAAkPUMRsi1HFLKjmr6yiDk18BAAMCAANzAAMzBA'
send_photo(URL, chat_id, photo)
