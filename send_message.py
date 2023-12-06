import requests
from settings import URL, chat_id


def send_message(url: str, chat_id: int, text: str, reply_markup: dict):
    endpoint = '/sendMessage'
    url += endpoint

    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup,
    }
    requests.post(url, json=data)

btn1 = {
    "text": "share contact",
    "request_contact": True
}
btn2 = {
    "text": "location",
    "request_location": True
}
btn3 = {"text": "button 3"}

reply_markup = {
    "keyboard": [
        [btn1, btn2],
        [btn3]
    ],
    "resize_keyboard": True,
    # "one_time_keyboard": True,
}

send_message(URL, chat_id, 'hi', reply_markup)
